def list_movies():
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetMovies", 
      "id": "list_movies", 
      "params": {
          "properties": ["file"]
        },
    }


def inspect_movie(movie_id):
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetMovieDetails", 
      "id": "movie_details",
      "params": {
          "movieid": int(movie_id),
          "properties": [
              "plotoutline", 
              "cast", "votes", "showlink", "year", "country", 
              "studio", "genre", "tag", "rating", "writer", "set",
              "originaltitle", "imdbnumber", "tagline", "title", "plot", "file",
              ],
        },
    }
