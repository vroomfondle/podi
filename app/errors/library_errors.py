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


class NoMediaError(Exception):
    """
    To be used when a media item can't be found.
    """

    def __init__(self, message):
        super(NoMediaError, self).__init__()
        self.error_message = message

    def __str__(self):
        return "Media not found: {0}".format(self.error_message)
