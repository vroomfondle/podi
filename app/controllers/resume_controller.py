from cement.core import controller
from lib.podi.rpc.library.movies import list_movies
from lib.podi.rpc.library.tv_shows import list_episodes
from lib.podi.rpc.player import play_file, play_movie, play_episode, enable_subtitles
from lib.podi.rpc.player import select_subtitle, list_active_players, select_audio, pause_unpause_player
from app.errors import JSONResponseError
import argparse

class ResumeController(controller.CementBaseController):
  class Meta:
    label = 'resume'
    description = 'Resume playback of a given media item (or play it from the start if not resumable).'
    stacked_on = 'base'
    stacked_type = 'nested'
    arguments = [(['positional_arguments'], dict(action = 'store', nargs = '*', help=argparse.SUPPRESS),),]

  @controller.expose(hide=True)
  def default(self):
    self.app.args.print_help()

  @controller.expose(aliases=['movies','film','films'],
    help='Play a movie, resuming at the last-watched timestamp if possible. You must provide a movie id number, e.g.: resume movie 127')
  def movie(self):
    try:
      movie_id = self.app.pargs.positional_arguments[0]
    except IndexError as e:
      self.app.log.error('You must provide a movie id number, e.g.: play movie 127')
      return False

    try:
      movie = [movie_details for movie_details in self.app.send_rpc_request(list_movies())['movies'] 
        if str(movie_details['movieid']) == movie_id][0]
    except IndexError as e:
      self.app.log.error("Movie {0} not found.".format(movie_id))
      return False
    self.app.log.info("Playing/resuming movie {0}: {1} ({2})".format(movie_id, movie['label'], movie['file']))
    self.app.send_rpc_request(play_movie(movie_id=movie_id, resume=True))


  @controller.expose(aliases=['tvepisode', 'tv_episode'],
    help='Play a TV episode, resuming at the last-watched timestamp if possible. You must provide an episode id number, e.g.: resume episode 1340')
  def episode(self):
    try:
      episode_id = self.app.pargs.positional_arguments[0]
    except IndexError as e:
      self.app.log.error('You must provide an episode id number, e.g.: play movie 127')
      return False
    self.app.log.info("Playing/resuming episode {0}".format(episode_id))
    try:
      self.app.send_rpc_request(play_episode(episode_id=episode_id, resume=True))
    except JSONResponseError as e:
      if e.error_code == -32602:
        self.app.log.error("Kodi returned an 'invalid parameters' error; this episode may not exist? Use 'list episodes' to  see available episodes.")
        return False
      else: raise e
  
