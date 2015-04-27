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
from cement.core import controller
from lib.podi.rpc.library import list_movies, inspect_movie, list_tv_shows,\
  list_episodes
from lib.podi.util import retrieve_sorted_episodes, retrieve_sorted_shows,\
  retrieve_sorted_movies, align_fields_for_display, format_runtime
import argparse



class ListController(controller.CementBaseController):
  _allowed_video_filters = ['genre', 'year', 'actor', 'director', 'studio', 'country', 'set', 'tag']

  class Meta:
    label = 'list'
    description = 'Retrieve and display lists of media items'
    stacked_on = 'base'
    stacked_type = 'nested'
    arguments = [
        (['positional_arguments'], dict(action = 'store', nargs = '*', help=argparse.SUPPRESS),),
      ]



  @controller.expose(hide=True)
  def default(self):
    self.app.args.print_help()



  @controller.expose(aliases=['films', 'movie', 'film'], help='Show a list of every movie in the system.')
  def movies(self):
    filters = self._parse_video_filters(self.app.pargs.positional_arguments[0:])
    field_widths = [('title', 36), ('movieid', 6)]
    movies = []
    for movie in retrieve_sorted_movies(rpc=self.app.send_rpc_request, filters=filters):
      movie['runtime'] = format_runtime(movie)
      movies.append(movie)
    movies = align_fields_for_display(movies, field_widths)
    print(self.app.render({'movies': sorted(movies, key = lambda movie: movie['movieid'])}, 'movie_list.m', None))



  @controller.expose(aliases=['show','tv_show','tv_shows','tv','tvshows','tvshow'], 
    help='Show a list of every TV show in the system.')
  def shows(self):
    filters = self._parse_video_filters(self.app.pargs.positional_arguments[0:])
    field_widths = [('title', 36),('tvshowid', 6),]
    shows = []
    for show in retrieve_sorted_shows(rpc=self.app.send_rpc_request, filters=filters):
      shows.append(show)
    shows = align_fields_for_display(shows, field_widths)
    print(self.app.render({'shows': shows}, 'tv_show_list.m', None))



  @controller.expose(aliases=['tv_episodes', 'tvepisodes','episode','tvepisode'], 
    help='Show a list of TV episodes for a particular show. A show id number must be provided (e.g. list episodes 152).')
  def episodes(self):
    """The user must provide a show id to restrict the list"""
    episodes = []
    try:
      show_id = self.app.pargs.positional_arguments[0]
    except IndexError:
      self.app.log.error("You must provide a show id (e.g. list episodes 152). Use 'list shows' to see all shows.")
      return False
    filters = self._parse_video_filters(self.app.pargs.positional_arguments[1:])
    for episode in retrieve_sorted_episodes(rpc=self.app.send_rpc_request, tv_show_id=show_id, filters=filters):
      episode['runtime'] = format_runtime(episode)
      episodes.append(episode)
    field_widths = [('title', 36),('episodeid', 6)]
    episodes = align_fields_for_display(episodes, field_widths)
    if len(episodes) > 0:
      print(self.app.render({'episodes': episodes},
        'episode_list.m', None))
    else:
      self.app.log.error("Kodi returned no episodes; this show may not exist? Use 'list shows' to see all shows.")




  def _parse_video_filters(self, args=[]):
    """Given a list of command-line args, this method turns them into a list of {key: value} filters 
    using alternate indexes, so ['genre', 'horror', 'actor', 'christopher lee'] becomes 
    [{'genre': 'horror'}, {'actor': 'christopher lee'}]. It also applies some validation to the filter keys,
    and raises a ValueError if an invalid filter is specified."""
    key = ''
    filters = []
    current_filter = {}
    for arg in args:
      if key != '':
        if key in self._allowed_video_filters:
          current_filter[key] = arg
          filters.append(current_filter)
          key = ''
        else:
          raise ValueError("Available filters: {0}".format(', '.join(allowed_keys)))
      else:
        key = arg
        
    return filters






