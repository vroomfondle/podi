from cement.core import controller
from lib.podi.rpc.library import inspect_movie
from lib.podi.rpc.library import list_episodes, inspect_episode, inspect_tv_show
from lib.podi.rpc.player import inspect_player, list_active_players
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
    pass

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

    movie_details['tag_dict'] = self._list_to_dicts(key = 'tag', input_list = movie_details['tag'])
    movie_details['genre_dict'] = self._list_to_dicts(key = 'genre', input_list = movie_details['genre'])
    movie_details['writer_dict'] = self._list_to_dicts(key = 'writer', input_list = movie_details['writer'])
    self.app.render(movie_details, 'movie_details.m')

    

  @controller.expose(aliases=['tv_show','tv','tvshow'], 
    help='Show information about a TV show. Provide the id number of the show (e.g. inspect show 9).')
  def show(self):
    try:
      tv_show_id = self.app.pargs.positional_arguments[0]
    except IndexError, e:
      self.app.log.error("You must provide a tv_show id number")
      return False
    try:
      tv_show_details = self.app.send_rpc_request(inspect_tv_show(tv_show_id))['tvshowdetails']
    except JSONResponseError, e:
      if e.error_code == -32602:
        self.app.log.error("Kodi returned an 'invalid parameters' error; this tv_show may not exist?")
        return False
      else: raise e
    tv_show_details['tag_dict'] = self._list_to_dicts(key = 'tag', input_list = tv_show_details['tag'])
    tv_show_details['genre_dict'] = self._list_to_dicts(key = 'genre', input_list = tv_show_details['genre'])
    tv_show_details['episodes'] = self._retrieve_sorted_episodes(tv_show_id)
    self.app.render(tv_show_details, 'tv_show_details.m')



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
    episode_details['writer_dict'] = self._list_to_dicts(key = 'writer', input_list = episode_details['writer'])
    self.app.render(episode_details, 'episode_details.m')


  @controller.expose(help='Show information about the currently-active media player')
  def player(self):
    for player in self.app.send_rpc_request(list_active_players()):
      player_details = self.app.send_rpc_request(inspect_player(player['playerid']))
      player_details['repeat'] = (player_details['repeat'] == 'on')
      self.app.log.debug(player_details)
      self.app.render(player_details, 'player_details.m')



  def _retrieve_sorted_episodes(self, tv_show_id):
    episodes =  self.app.send_rpc_request(list_episodes(tv_show_id)).get('episodes', [])
    for episode in sorted(
      episodes,
      key = lambda episode: episode['episodeid']):
      yield episode



  def _list_to_dicts(self, key, input_list):
    return [{key: x} for x in input_list]
