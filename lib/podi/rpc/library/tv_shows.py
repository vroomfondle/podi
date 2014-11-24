def list_tv_shows():
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetTVShows", 
      "id": "list_shows", 
      "params": {
          "properties": [
            "file", "title", "originaltitle",
            "genre", "year", "tag",
            "studio", "cast", "imdbnumber",
            "mpaa", "playcount", "rating", 
            "votes", "sorttitle", "dateadded",
            "lastplayed",
          ]
        },
    }



def list_episodes(tv_show_id = None):
  request = {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetEpisodes", 
      "id": "list_episodes_{0}".format(tv_show_id), 
      "params": {
          "properties": [
            "file", "title", "originaltitle",
            "writer",  "director",
            "cast", 
            "rating", "playcount",
            "votes", "dateadded",
            "lastplayed", "resume", "runtime",
            "productioncode", "firstaired",
            "season", "episode",
          ],
          "tvshowid": int(tv_show_id),
        },
  }
  if tv_show_id is not None:
    request["params"]["tvshowid"] = int(tv_show_id)
  return request


def inspect_episode(episode_id):
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetEpisodeDetails", 
      "id": "episode_details",
      "params": {
          "episodeid": int(episode_id),
          "properties": [
              "cast", "votes", "firstaired", "season", "showtitle",
              "rating", "writer", "title", "file",
              "originaltitle", "productioncode", "playcount",
              ],
        },
    }


def inspect_tv_show(tv_show_id):
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.GetTVShowDetails", 
      "id": "tv_show_details",
      "params": {
          "tvshowid": int(tv_show_id),
          "properties": [
                "title", "cast", "votes", "mpaa", "rating",
                "studio", "genre", "episodeguide", "tag", "year",
                "originaltitle", "imdbnumber", "plot", "lastplayed",
              ],
        },
    }
