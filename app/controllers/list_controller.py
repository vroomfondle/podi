from cement.core import controller
from lib.podi.rpc.library import list_movies, inspect_movie
from lib.podi.rpc.library import list_tv_shows, list_episodes
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
    movies = self._align_fields_for_display(self.app.send_rpc_request(list_movies())['movies'], field_widths)
    print self.app.render({'movies': sorted(movies, key = lambda movie: movie['movieid'])}, 'movie_list.m', None).encode('utf8')


  @controller.expose(aliases=['show','tv_show','tv_shows','tv','tvshows','tvshow'], 
    help='Show a list of every TV show in the system.')
  def shows(self):
    field_widths = [('title', 36),('tvshowid', 6),]
    shows = []
    for show in self._retrieve_sorted_shows():
      shows.append(show)
    shows = self._align_fields_for_display(shows, field_widths)
    print self.app.render({'shows': shows}, 'tv_show_list.m', None).encode('utf8')


  @controller.expose(aliases=['tv_episodes', 'tvepisodes','episode','tvepisode'], 
    help='Show a list of TV episodes for a particular show. A show id number must be provided (e.g. list episodes 152).')
  def episodes(self):
    """The user must provide a show id to restrict the list"""
    episodes = []
    try:
      show_id = self.app.pargs.positional_arguments[0]
    except IndexError:
      self.app.log.error("You must provide a show id (e.g. list episodes 152).")
      return False
    for ep in self._retrieve_sorted_episodes(show_id):
      episodes.append(ep)
    field_widths = [('title', 36),('episodeid', 6)]
    episodes = self._align_fields_for_display(episodes, field_widths)
    if len(episodes) > 0:
      print self.app.render({'episodes': episodes},
        'episode_list.m', None).encode('utf8')
    else:
      self.app.log.error("Kodi returned no episodes; this show may not exist? Use 'list shows' to see all shows.")


  def _retrieve_sorted_shows(self, tv_show_id = None):
    shows = self.app.send_rpc_request(list_tv_shows())['tvshows']
    for show in sorted(shows, key = lambda show: show['tvshowid']):
      if (tv_show_id is None) or int(show['tvshowid']) == int(tv_show_id): 
        yield show


  def _retrieve_sorted_episodes(self, tv_show_id):
    episodes =  self.app.send_rpc_request(list_episodes(tv_show_id)).get('episodes', [])
    for episode in sorted(
      episodes,
      key = lambda episode: episode['episodeid']):
      yield episode


  def _align_fields_for_display(self, items, fields):
    """
    Pads/truncates fields in each item to the specified length and puts the result in index ('display'+field_name).
    fields should be a list of tuples (str,int): (field_name, length)  
    """
    for item in items:
      for (field_name, length) in fields:
        if type(item[field_name]) is str or type(item[field_name]) is unicode:
          field_value = item[field_name]
        else:
          field_value = str(item[field_name])
        item['display{0}'.format(field_name)] = field_value[0:length-1].ljust(length)
    return items




