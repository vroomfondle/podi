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
from lib.podi.rpc.library import clean_video_library, clean_audio_library


class CleanupController(controller.CementBaseController):
    """
    Sends RPC calls to Kodi to tell it to clean up its media libraries.
    """

    class Meta:
        """
        Defines metadata for use by the Cement framework.
        """

        label = 'cleanup'
        aliases = ['tidy', 'clean']
        description = 'Clean up media libraries by removing non-existent items'
        stacked_on = 'base'
        stacked_type = 'nested'

    @controller.expose(hide=True)
    def default(self):
        """
        Instructs Kodi to clean up its media libraries.
        """

        self.app.log.info("Cleaning up video library")
        self.app.send_rpc_request(clean_video_library())
        self.app.log.info("Cleaning up audio library")
        self.app.send_rpc_request(clean_audio_library())
