from cement.core import controller
from lib.podi.rpc.library.movies import list_movies
from lib.podi.rpc.library.tv_shows import list_tv_shows
from lib.podi.rpc.player import play_file

class PlayController(controller.CementBaseController):
  class Meta:
    label = 'play'
    description = 'Trigger playback of a given media item'
    stacked_on = 'base'
    stacked_type = 'nested'
    arguments = [(['positional_arguments'], dict(action = 'store', nargs = '*')),]

  @controller.expose(hide=True)
  def default(self):
    pass

  @controller.expose()
  def movie(self):
    id = self.app.pargs.positional_arguments[0]
    try:
      movie = [movie_details for movie_details in self.app.send_rpc_request(list_movies())['result']['movies'] 
        if str(movie_details['movieid']) == id][0]
    except IndexError, e:
      self.app.log.error("Movie {0} not found.".format(id))
      return False
    # Movie exists if no AttributeError was thrown; try to play it
    self.app.log.info("Playing movie {0}: {1} ({2})".format(id, movie['label'], movie['file']))
    self.app.send_rpc_request(play_file(movie['file']))


  @controller.expose(aliases=['tv', 'tvshow', 'show'])
  def tv_show(self):
    id = self.app.pargs.positional_arguments[0]
    try:
      tvshow = [tvshow_details for tvshow_details in self.app.send_rpc_request(list_tv_shows())['result']['tvshows'] 
        if str(tvshow_details['tvshowid']) == id][0]
    except IndexError, e:
      self.app.log.error("Movie {0} not found.".format(id))
      return False
    # Movie exists if no AttributeError was thrown; try to play it
    self.app.log.info("Playing tvshow {0}: {1} ({2})".format(id, tvshow['label'], tvshow['file']))
    self.app.send_rpc_request(play_file(tvshow['file']))
