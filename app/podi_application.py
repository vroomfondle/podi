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
from cement.core import foundation, controller
from http.client import HTTPConnection
from urllib.parse import quote
from os.path import expanduser, dirname
from .errors import JSONResponseError
from lib.podi.rpc import rpc_version
import json


class PodiBase(controller.CementBaseController):

    class Meta:
        label = 'base'

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        print('Use --help to see a list of commands')


class PodiApplication(foundation.CementApp):

    class Meta:
        label = 'podi'
        description = 'Podi'
        base_controller = PodiBase
        config_files = ["%s/.podi.conf" % expanduser("~")]
        extensions = ['mustache', 'json', 'yaml']
        output_handler = 'mustache'
        template_dir = "{0}/views".format(dirname(__file__))

    def __init__(self, **kwargs):
        super(PodiApplication, self).__init__(**kwargs)

    def run(self):
        self.connection = HTTPConnection(self.config.get('connection', 'host'),
                                         self.config.get('connection', 'port'))
        self.send_rpc_request(rpc_version())
        super(PodiApplication, self).run()

    def send_rpc_request(self, request):
        """
        Sends an RPC request to the remote host.
        :param dict request 
        """
        headers = {"Content-type": "application/json"}
        self.log.debug("Sending RPC request: {0}".format(request))
        self.connection.request(
            "GET", "/jsonrpc?request=%s" % quote(json.dumps(request), ''), None, headers)
        response_text = self.connection.getresponse().read().decode('utf-8')
        self.log.debug("Received RPC response: {0}".format(response_text))
        response = json.loads(response_text)
        if response.get('error', False):
            # Found an error - throw exception
            raise JSONResponseError(response)
        return response.get('result', None)
