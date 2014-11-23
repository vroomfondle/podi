from cement.core import controller
from lib.podi.rpc.player import pause_unpause_player, list_active_players
import argparse

class PauseController(controller.CementBaseController):
  class Meta:
    label = 'pause'
    aliases = ['unpause']
    description = 'Pause/unpause the current media item'
    stacked_on = 'base'
    stacked_type = 'nested'

  @controller.expose(hide=True)
  def default(self):
    for player in self.app.send_rpc_request(list_active_players()):
      self.app.log.info("Pausing/unpausing {0}".format(player['type']))
      self.app.send_rpc_request(pause_unpause_player(player['playerid']))


  
