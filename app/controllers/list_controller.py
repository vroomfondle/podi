from cement.core import controller
from lib.podi.rpc.library.movies import list_movies
from lib.podi.rpc.library.tv_shows import list_tv_shows, list_episodes

class ListController(controller.CementBaseController):
  class Meta:
    label = 'list'
    description = 'Retrieve and display lists of media items'
    stacked_on = 'base'
    stacked_type = 'nested'

  @controller.expose(hide=True)
  def default(self):
    pass

  @controller.expose()
  def movies(self):
    movies = self.app.send_rpc_request(list_movies())['movies']
    for movie in sorted(movies, key = lambda movie: movie['movieid']):
      print "{0}\t{1}".format(movie['movieid'], movie['label'].encode('utf8'))


  @controller.expose(aliases=['shows','tv','tvshows'])
  def tv_shows(self):
    for show in self._retrieve_sorted_shows():
      print "Show:\t{0}\t{1}".format(show['tvshowid'], show['label'].encode('utf8'))



  @controller.expose(aliases=['episodes', 'tvepisodes'])
  def tv_episodes(self):
    for show in self._retrieve_sorted_shows():
      print "Show:\t{0}\t{1}".format(show['tvshowid'], show['label'].encode('utf8'))
      for episode in self._retrieve_sorted_episodes(show['tvshowid']):
        print "\tEpisode:\t{0}\t{1}".format(
            episode['episodeid'], 
            episode['label'],
          )


  def _retrieve_sorted_shows(self):
    shows = self.app.send_rpc_request(list_tv_shows())['tvshows']
    for show in sorted(shows, key = lambda show: show['tvshowid']):
      yield show


  def _retrieve_sorted_episodes(self, tv_show_id):
    episodes =  self.app.send_rpc_request(list_episodes(tv_show_id)).get('episodes', [])
    for episode in sorted(
      episodes,
      key = lambda episode: episode['episodeid']):
      yield episode
