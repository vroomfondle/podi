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
from lib.podi.rpc.library import update_video_library, update_audio_library
import argparse


class UpdateController(controller.CementBaseController):

    class Meta:
        label = 'update'
        aliases = ['scan']
        description = 'Update media libraries by scanning for new files'
        stacked_on = 'base'
        stacked_type = 'nested'

    @controller.expose(hide=True)
    def default(self):
        self.app.log.info("Updating videos")
        self.app.send_rpc_request(update_video_library())
        self.app.log.info("Updating audio")
        self.app.send_rpc_request(update_audio_library())
