def introspect_method(method_name):
  """Can be used to retrieve documentation for the given JSON RPC method"""
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
  return {
      "jsonrpc": "2.0",
      "method": "JSONRPC.Version",
      "id": "rpc_version"
  }
