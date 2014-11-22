def list_tv_shows(id = None):
  if id is None:
    filter = {}
  else:
    filter = {"field": "tvshowid", "operator": "is", "value": "{0}".format(id)}

  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetTVShows", 
      "id": "list_shows", 
      "params": {
          "properties": ["file"],
          "filter": filter
        },
    }
