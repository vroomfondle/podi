from cement.core import controller
from lib.podi.rpc.player import stop_player, list_active_players
import argparse

class StopController(controller.CementBaseController):
  class Meta:
    label = 'stop'
    description = 'Stop playing the current media item'
    stacked_on = 'base'
    stacked_type = 'nested'

  @controller.expose(hide=True)
  def default(self):
    for player in self.app.send_rpc_request(list_active_players()):
      self.app.log.info("Stopping {0}".format(player['type']))
      self.app.send_rpc_request(stop_player(player['playerid']))


  
