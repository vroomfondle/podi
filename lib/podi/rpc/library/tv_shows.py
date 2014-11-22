def list_tv_shows():
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetTVShows", 
      "id": "list_shows", 
      "params": {
          "properties": ["file"],
          "filter": filter
        },
    }
