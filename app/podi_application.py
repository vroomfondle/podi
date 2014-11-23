from cement.core import foundation, controller
from httplib import HTTPConnection
from urllib import quote
from os.path import expanduser, dirname
from errors import JSONResponseError
from lib.podi.rpc import rpc_version
import json

class PodiBase(controller.CementBaseController):
  class Meta:
    label = 'base'


  @controller.expose(hide=True, aliases=['run'])
  def default(self):
    print 'Use --help to see a list of commands'
    

class PodiApplication(foundation.CementApp):
  class Meta:
    label = 'podi'
    description = 'Podi'
    base_controller = PodiBase
    config_files = ["%s/.podi.conf" % expanduser("~")]
    extensions = ['mustache']
    output_handler = 'mustache'
    template_dir = "{0}/views".format(dirname(__file__))



  def  __init__(self):
    super(PodiApplication, self).__init__()



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
    headers={"Content-type": "application/json"}
    self.log.debug("Sending RPC request: {0}".format(request))
    self.connection.request("GET", "/jsonrpc?request=%s" % quote(json.dumps(request), ''), None, headers)
    response_text = self.connection.getresponse().read()
    self.log.debug("Received RPC response: {0}".format(response_text))
    response = json.loads(response_text)
    if response.get('error', False):
      # Found an error - throw exception
      raise JSONResponseError(response)
    return response.get('result', None)
    
