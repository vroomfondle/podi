from cement.core import controller
from lib.podi.rpc.library import list_movies, inspect_movie
from lib.podi.rpc.library import list_tv_shows, list_episodes
from lib.podi.util import retrieve_sorted_episodes, retrieve_sorted_shows, align_fields_for_display
import argparse

class ListController(controller.CementBaseController):
  class Meta:
    label = 'list'
    description = 'Retrieve and display lists of media items'
    stacked_on = 'base'
    stacked_type = 'nested'
    arguments = [(['positional_arguments'], dict(action = 'store', nargs = '*', help=argparse.SUPPRESS),),]

  @controller.expose(hide=True)
  def default(self):
    self.app.args.print_help()


  @controller.expose(aliases=['films', 'movie', 'film'], help='Show a list of every movie in the system.')
  def movies(self):
    field_widths = [('title', 36), ('movieid', 6)]
    movies = self.align_fields_for_display(self.app.send_rpc_request(list_movies())['movies'], field_widths)
    print self.app.render({'movies': sorted(movies, key = lambda movie: movie['movieid'])}, 'movie_list.m', None).encode('utf8')


  @controller.expose(aliases=['show','tv_show','tv_shows','tv','tvshows','tvshow'], 
    help='Show a list of every TV show in the system.')
  def shows(self):
    field_widths = [('title', 36),('tvshowid', 6),]
    shows = []
    for show in self._retrieve_sorted_shows():
      shows.append(show)
    shows = self.align_fields_for_display(shows, field_widths)
    print self.app.render({'shows': shows}, 'tv_show_list.m', None).encode('utf8')


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
    for ep in retrieve_sorted_episodes(show_id, self.app.send_rpc_request):
      episodes.append(ep)
    field_widths = [('title', 36),('episodeid', 6)]
    episodes = self.align_fields_for_display(episodes, field_widths)
    if len(episodes) > 0:
      print self.app.render({'episodes': episodes},
        'episode_list.m', None).encode('utf8')
    else:
      self.app.log.error("Kodi returned no episodes; this show may not exist? Use 'list shows' to see all shows.")

  




