from cement.core import controller
from lib.podi.rpc.library import inspect_movie
from lib.podi.rpc.library import list_episodes, inspect_episode, inspect_tv_show
from lib.podi.rpc.player import inspect_player, list_active_players, inspect_current_item
from lib.podi.util import retrieve_sorted_episodes, list_to_dicts
from app.errors import JSONResponseError
from functools import partial
import argparse

class InspectController(controller.CementBaseController):
  class Meta:
    label = 'inspect'
    description = 'Retrieve and display inspects of media items'
    stacked_on = 'base'
    stacked_type = 'nested'
    arguments = [(['positional_arguments'], dict(action = 'store', nargs = '*', help=argparse.SUPPRESS),),]



  @controller.expose(hide=True)
  def default(self):
    self.app.args.print_help()



  @controller.expose(aliases=['film'], help='Show information about a movie. Provide the id number of the movie (e.g. inspect movie 107).')
  def movie(self):
    try:
      movie_id = self.app.pargs.positional_arguments[0]
    except IndexError, e:
      self.app.log.error("You must provide a movie id number")
      return False
    try:
      movie_details = self.app.send_rpc_request(inspect_movie(movie_id))['moviedetails']
    except JSONResponseError, e:
      if e.error_code == -32602:
        self.app.log.error("Kodi returned an 'invalid parameters' error; this movie may not exist?")
        return False
      else: raise e
    list_to_dicts(key = 'tag', input_list = movie_details['tag'])
    list_to_dicts(key = 'genre', input_list = movie_details['genre'])
    list_to_dicts(key = 'writer', input_list = movie_details['writer'])
    list_to_dicts(key = 'country', input_list = movie_details['country'])
    print self.app.render(movie_details, 'movie_details.m', None).encode('utf8')
   


  @controller.expose(aliases=['tv_show','tv','tvshow'], 
    help='Show information about a TV show. Provide the id number of the show (e.g. inspect show 9).')
  def show(self):
    try:
      tv_show_id = self.app.pargs.positional_arguments[0]
    except IndexError, e:
      self.app.log.error("You must provide a show id number")
      return False
    try:
      tv_show_details = self.app.send_rpc_request(inspect_tv_show(tv_show_id))['tvshowdetails']
    except JSONResponseError, e:
      if e.error_code == -32602:
        self.app.log.error("Kodi returned an 'invalid parameters' error; this tv_show may not exist?")
        return False
      else: raise e
    list_to_dicts(key = 'tag', input_list = tv_show_details['tag'])
    list_to_dicts(key = 'genre', input_list = tv_show_details['genre'])
    tv_show_details['episodes'] = retrieve_sorted_episodes(self.app.send_rpc_request, tv_show_id)
    print self.app.render(tv_show_details, 'tv_show_details.m', None).encode('utf8')



  @controller.expose(aliases=['tv_episode','tvepisode'], 
    help='Show information about a TV show episode. Provide an episode id number (e.g. inspect episode 155).')
  def episode(self):
    try:
      episode_id = self.app.pargs.positional_arguments[0]
    except IndexError, e:
      self.app.log.error("You must provide a episode id number")
      return False
    try:
      episode_details = self.app.send_rpc_request(inspect_episode(episode_id))['episodedetails']
    except JSONResponseError, e:
      if e.error_code == -32602:
        self.app.log.error("Kodi returned an 'invalid parameters' error; this episode may not exist?")
        return False
      else: raise e
    list_to_dicts(key = 'writer', input_list = episode_details['writer'])
    print self.app.render(episode_details, 'episode_details.m', None).encode('utf8')



  @controller.expose(help='Show information about the currently-active media player, including available audio and subtitle streams.')
  def player(self):
    for player in self.app.send_rpc_request(list_active_players()):
      player_details = self.app.send_rpc_request(inspect_player(player['playerid']))
      player_details['repeat'] = (player_details['repeat'] == 'on')
      self.app.log.debug(player_details)
      player_details['item'] = self.app.send_rpc_request(inspect_current_item(player['playerid']))['item']
      print self.app.render(player_details, 'player_details.m', None).encode('utf8')



