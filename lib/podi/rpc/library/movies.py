def list_movies():
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetMovies", 
      "id": "list_movies", 
      "params": {
          "properties": ["file"]
        },
    }
