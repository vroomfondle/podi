def list_tv_shows():
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetTVShows", 
      "id": "list_shows", 
      "params": {
          "properties": ["file"],
        },
    }



def list_episodes(tv_show_id = None):
  request = {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetEpisodes", 
      "id": "list_episodes_{0}".format(tv_show_id), 
      "params": {
          "properties": ["file"],
        },
  }
  if tv_show_id is not None:
    request["params"]["tvshowid"] = int(tv_show_id)
  return request
