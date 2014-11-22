from cement.core import controller
from lib.podi.rpc.library.movies import list_movies
from lib.podi.rpc.library.tv_shows import list_episodes
from lib.podi.rpc.player import play_file, play_movie, play_episode

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

  @controller.expose(aliases=['movies','film','films'],
    help='Play a movie. You must provide a movie id number, e.g.: play movie 127')
  def movie(self):
    try:
      movie_id = self.app.pargs.positional_arguments[0]
    except IndexError, e:
      self.app.log.error('You must provide a movie id number, e.g.: play movie 127')
      return False

    try:
      movie = [movie_details for movie_details in self.app.send_rpc_request(list_movies())['movies'] 
        if str(movie_details['movieid']) == movie_id][0]
    except IndexError, e:
      self.app.log.error("Movie {0} not found.".format(movie_id))
      return False
    # Movie exists if no AttributeError was thrown; try to play it
    self.app.log.info("Playing movie {0}: {1} ({2})".format(movie_id, movie['label'], movie['file']))
    self.app.send_rpc_request(play_movie(movie_id))


  @controller.expose(aliases=['tvepisode', 'tv_episode'],
    help='Play a movie. You must provide an episode id number, e.g.: play episode 1340')
  def episode(self):
    tv_episode_id = self.app.pargs.positional_arguments[0]
    try:
      episode = [episode_details for episode_details in self.app.send_rpc_request(list_episodes())['episodes'] 
        if str(episode_details['episodeid']) == tv_episode_id][0]
    except IndexError, e:
      self.app.log.error("Episode {0} not found.".format(episode_id))
      return False
    # Movie exists if no AttributeError was thrown; try to play it
    self.app.log.info("Playing episode {0}: {1} ({2})".format(tv_episode_id, episode['label'], episode['file']))
    self.app.send_rpc_request(play_episode(tv_episode_id))
  
