class JSONResponseError(Exception):
  def __init__(self, json_response):
    self.error_message = json_response['error']['message']
    self.error_code = json_response['error']['code']
    self.json_response = json_response

  def __str__(self):
    return repr("Kodi JSON RPC error {0}: {1}".format(self.error_code, self.error_message))
