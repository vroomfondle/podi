"""
    Podi, a command-line interface for Kodi.
    Copyright (C) 2015  Peter Frost <slimeypete@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from cement.core import controller
from lib.podi.rpc.player import pause_unpause_player, list_active_players


class PauseController(controller.CementBaseController):
    """
    Sends RPC calls to Kodi to pause playback of media items.
    """

    class Meta:
        """
        Defines metadata for use by the Cement framework.
        """

        label = 'pause'
        aliases = ['unpause']
        description = 'Pause/unpause the current media item'
        stacked_on = 'base'
        stacked_type = 'nested'

    @controller.expose(hide=True)
    def default(self):
        """
        Instructs Kodi to pause the current media item.
        """

        for player in self.app.send_rpc_request(list_active_players()):
            self.app.log.info("Pausing/unpausing {0}".format(player['type']))
            self.app.send_rpc_request(pause_unpause_player(player['playerid']))
