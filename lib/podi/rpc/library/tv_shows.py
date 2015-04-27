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


def list_tv_shows(filters=None):
    return {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetTVShows",
        "id": "list_shows",
        "params": {
            "properties": [
              "file", "title", "originaltitle",
              "genre", "year", "tag",
              "studio", "cast", "imdbnumber",
              "mpaa", "playcount", "rating",
              "votes", "sorttitle", "dateadded",
              "lastplayed",
            ]
        },
    }


def list_episodes(tv_show_id=None, filters=None):
    request = {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetEpisodes",
        "id": "list_episodes_{0}".format(tv_show_id),
        "params": {
            "properties": [
              "file", "title", "originaltitle",
              "writer",  "director",
              "cast",
              "rating", "playcount",
              "votes", "dateadded",
              "lastplayed", "resume", "runtime",
              "productioncode", "firstaired",
              "season", "episode",
            ],
            "tvshowid": int(tv_show_id),
        },
    }
    if tv_show_id is not None:
        request["params"]["tvshowid"] = int(tv_show_id)
    return request


def inspect_episode(episode_id):
    return {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetEpisodeDetails",
        "id": "episode_details",
        "params": {
            "episodeid": int(episode_id),
            "properties": [
                "cast", "votes", "firstaired", "season", "showtitle",
                "rating", "writer", "title", "file", "plot",
                "originaltitle", "productioncode", "playcount",
            ],
        },
    }


def inspect_tv_show(tv_show_id):
    return {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetTVShowDetails",
        "id": "tv_show_details",
        "params": {
            "tvshowid": int(tv_show_id),
            "properties": [
                  "title", "cast", "votes", "mpaa", "rating",
                  "studio", "genre", "episodeguide", "tag", "year",
                  "originaltitle", "imdbnumber", "plot", "lastplayed",
            ],
        },
    }
