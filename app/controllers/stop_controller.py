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
from lib.podi.rpc.player import stop_player, list_active_players, disable_subtitles
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

    @controller.expose(aliases=['subtitles'], help='Disable subtitles.')
    def subtitle(self):
        for player in self.app.send_rpc_request(list_active_players()):
            self.app.send_rpc_request(disable_subtitles(player['playerid']))
