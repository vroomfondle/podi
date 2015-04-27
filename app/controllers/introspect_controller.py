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
from lib.podi.rpc import introspect_method


class IntrospectController(controller.CementBaseController):
    """
    Sends RPC calls to Kodi to retrieve details about Kodi itself.
    """

    class Meta:
        """
        Defines metadata for use by the Cement framework.
        """

        label = 'introspect'
        description = "Show details of Kodi's JSON RPC methods via introspection"
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [
            (['positional_arguments'], dict(action='store', nargs='*')), ]

    @controller.expose(hide=True)
    def default(self):
        """
        Prints the help text when the user has supplied no arguments.
        """

        self.app.args.print_help()

    @controller.expose()
    def method(self):
        """
        Instructs Kodi to describe the RPC method specified by the user.
        """

        method_name = self.app.pargs.positional_arguments[0]
        response = self.app.send_rpc_request(introspect_method(method_name))
        print(self.app.render(
            response['methods'][method_name], 'method_introspection.m', None))
