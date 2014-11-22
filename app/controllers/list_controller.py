from cement.core import controller
from lib.podi.rpc.library.movies import list_movies
from lib.podi.rpc.library.tv_shows import list_tv_shows

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
    movies = self.app.send_rpc_request(list_movies())['result']['movies']
    for movie in sorted(movies, key = lambda movie: movie['movieid']):
        print "{0} - {1}".format(movie['movieid'], movie['label'].encode('utf8'))


  @controller.expose(aliases=['shows','tv','tvshows'])
  def tv_shows(self):
    shows = self.app.send_rpc_request(list_tv_shows())['result']['tvshows']
    for show in sorted(shows, key = lambda show: show['tvshowid']):
        print "{0} - {1}".format(show['tvshowid'], show['label'].encode('utf8'))
