from cement.core import controller
from lib.podi.rpc.library.movies import list_movies
from lib.podi.rpc.library.tv_shows import list_tv_shows, list_episodes

class ListController(controller.CementBaseController):
  class Meta:
    label = 'list'
    description = 'Retrieve and display lists of media items'
    stacked_on = 'base'
    stacked_type = 'nested'
    arguments = [(['positional_arguments'], dict(action = 'store', nargs = '*')),]

  @controller.expose(hide=True)
  def default(self):
    pass

  @controller.expose(aliases=['films', 'movie', 'film'], help='Show a list of every movie in the system.')
  def movies(self):
    movies = self.app.send_rpc_request(list_movies())['movies']
    for movie in sorted(movies, key = lambda movie: movie['movieid']):
      print "{0}\t{1}".format(movie['movieid'], movie['label'].encode('utf8'))


  @controller.expose(aliases=['show','tv_show','tv_shows','tv','tvshows','tvshow'], 
    help='Show a list of every TV show in the system.')
  def shows(self):
    for show in self._retrieve_sorted_shows():
      print "Show:\t{0}\t{1}".format(show['tvshowid'], show['label'].encode('utf8'))



  @controller.expose(aliases=['tv_episodes', 'tvepisodes','episode','tvepisode'], 
    help='Show a list of TV episodes. If a show id number is provided (e.g. list episodes 152) then only episodes '
    'of that show will be listed; if the id number is ommitted, episodes will be listed for all shows in the system.')
  def episodes(self):
    """The user may optionally provide a show id to restrict the list"""
    show_id = None
    try:
      show_id = self.app.pargs.positional_arguments[0]
    except IndexError:
      self.app.log.debug("Show id not provided")

    for show in self._retrieve_sorted_shows(show_id):
      print "Show:\t{0}\t{1}".format(show['tvshowid'], show['label'].encode('utf8'))
      for episode in self._retrieve_sorted_episodes(show['tvshowid']):
        print "\tEpisode:\t{0}\t{1}".format(
            episode['episodeid'], 
            episode['label'],
          )


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
