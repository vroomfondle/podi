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


def introspect_method(method_name):
    """
    Can be used to retrieve documentation for the given JSON RPC method
    :param method_name The fully-qualified name of the method.
    """
    if method_name == "" or method_name is None:
        raise ValueError("Method name must not be empty")

    return {
        "jsonrpc": "2.0",
        "method": "JSONRPC.Introspect",
        "params": {
            "filter": {
                "id": method_name,
                "type": "method"
            }
        },
        "id": "introspect_{0}".format(method_name)
    }


def rpc_version():
    """
    :returns A dict representing the JSON RPC call to ask Kodi what RPC version it supports.
    """
    return {
        "jsonrpc": "2.0",
        "method": "JSONRPC.Version",
        "id": "rpc_version"
    }
