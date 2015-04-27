"""
    Podi, a command-line interface for Kodi.
    Copyright (C) 2015  Peter Frost <slimeypete@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from ..rpc.library import list_episodes, list_tv_shows, list_movies

SORT_ASC = 1
SORT_DESC = 2


def retrieve_sorted_episodes(rpc, tv_show_id, sort_field='episodeid', sort_order=SORT_ASC, filters=None):
    """rpc should be a callable which will send the JSONRPC request to the Kodi server"""
    episodes = rpc(list_episodes(tv_show_id, filters=filters)).get(
        'episodes', [])
    for episode in sorted(
            episodes,
            key=lambda episode: episode[sort_field]):
        yield episode


def retrieve_sorted_movies(rpc, sort_field='movieid', sort_order=SORT_ASC, filters=None):
    """rpc should be a callable which will send the JSONRPC request to the Kodi server"""
    movies = rpc(list_movies(filters=filters)).get('movies', [])
    for movie in sorted(
            movies,
            key=lambda movie: movie[sort_field]):
        yield movie


def retrieve_sorted_shows(rpc, tv_show_id=None, sort_field='tvshowid', sort_order=SORT_ASC, filters=None):
    """rpc should be a callable which will send the JSONRPC request to the Kodi server. tv_show_id can be used to restrict the list to a single id."""
    shows = rpc(list_tv_shows(filters=filters)).get('tvshows', [])
    for show in sorted(shows, key=lambda show: show[sort_field]):
        if (tv_show_id is None) or int(show['tvshowid']) == int(tv_show_id):
            yield show


def list_to_dicts(key, input_list):
    """Turns a list of values into a list of single-entry dicts, with the provided key,
    so that the dicts can be used with pystache. The list is modified in-place."""
    for index in range(len(input_list)):
        input_list[index] = {key: input_list[index]}


def align_fields_for_display(items, fields):
    """
    Pads/truncates fields in each item to the specified length and puts the result in index ('display'+field_name).
    fields should be a list of tuples (str,int): (field_name, length).
    Returns the input list with padded items.
    """
    for item in items:
        for (field_name, length) in fields:
            if isinstance(item[field_name], str) or isinstance(item[field_name], str):
                field_value = item[field_name]
            else:
                field_value = str(item[field_name])
            item['display{0}'.format(field_name)] = field_value[
                0:length - 1].ljust(length)
    return items


def format_runtime(video_item):
    """
    Finds the longest video stream in a given item, and returns a dict:
      {'total_seconds':n, 'hours':n, 'minutes':n, 'seconds':n, 'str':"{hours}:{minutes}:{seconds}"}.
    video_item should be an item as returned in response to the JSON defined by the lib.podi.rpc.library methods,
    and should include a sub-dict called 'streamdetails'.
    If the 'streamdetails' sub-dict is entirely missing, expect to see an IndexError.
    """
    minutes, seconds = divmod(int(video_item['runtime']), 60)
    hours, minutes = divmod(minutes, 60)
    return {
        'total_seconds': video_item['runtime'],
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'str': "{0:02d}:{1:02d}:{2:02d}".format(hours, minutes, seconds),
    }
