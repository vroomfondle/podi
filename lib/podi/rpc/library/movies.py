def list_movies():
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetMovies", 
      "id": "list_movies", 
      "params": {
          "properties": [
            "file", "title", "originaltitle",
            "genre", "year", "tag",
            "director", "studio", "cast", "imdbnumber",
            "mpaa", "playcount", "rating", 
            "runtime", "set", "showlink", "top250",
            "votes", "sorttitle", "resume", "setid", "dateadded",
          ],
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
            "file", "title", "originaltitle",
            "genre", "year", "tag", "tagline", "writer",
            "director", "studio", "cast", "imdbnumber", "country",
            "mpaa", "playcount", "rating", "plot", "plotoutline",
            "runtime", "set", "showlink", "streamdetails", "top250",
            "votes", "sorttitle", "resume", "setid", "dateadded",
          ],
        },
    }
