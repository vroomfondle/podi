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


class MissingArgumentError(Exception):
    """
    Represents an error which has been recieved from Kodi's Argument RPC mechanism.
    """

    def __init__(self, missing_arg_name, extra_explanation):
        super(MissingArgumentError, self).__init__()
        self.missing_arg_name = missing_arg_name
        self.explanation = extra_explanation

    def __str__(self):
        return repr("Missing argument: {0}. {1}".format(self.missing_argument, self.explanation))
