def list_movies(id = None):
  if id is None:
    filter = {}
  else:
    filter = {"field": "movieid", "operator": "is", "value": id}

  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetMovies", 
      "id": "list_movies", 
      "params": {
          "properties": ["file"],
          "filter": filter
        },
    }
