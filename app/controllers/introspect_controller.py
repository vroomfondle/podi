from cement.core import controller
from lib.podi.rpc import introspect_method
import json

class IntrospectController(controller.CementBaseController):
  class Meta:
    label = 'introspect'
    description = "Show details of Kodi's JSON RPC methods via introspection"
    stacked_on = 'base'
    stacked_type = 'nested'
    arguments = [(['positional_arguments'], dict(action = 'store', nargs = '*')),]

  @controller.expose(hide=True)
  def default(self):
    pass

  @controller.expose()
  def method(self):
    method_name = self.app.pargs.positional_arguments[0]
    response = self.app.send_rpc_request(introspect_method(method_name))
    print json.dumps(response, indent=4)
