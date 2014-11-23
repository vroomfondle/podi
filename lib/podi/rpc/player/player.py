from types import DictType

def play_file(file_path):
  return {
      "jsonrpc": "2.0",
      "method": "Player.Open",
      "params": {
            "item": {"file": file_path}
      },
      "id": "play_file"
  }

def play_movie(movie_id):
  return {
      "jsonrpc": "2.0",
      "method": "Player.Open",
      "params": {
            "item": {"movieid": int(movie_id)}
      },
      "id": "play_movie_{0}".format(movie_id)
  }

def play_episode(episode_id):
  return {
      "jsonrpc": "2.0",
      "method": "Player.Open",
      "params": {
         "item": {"episodeid": int(episode_id)}
      },
      "id": "play_tv_episode_{0}".format(episode_id)
  }

def pause_unpause_player(player_id):
  return {
    "jsonrpc": "2.0",
    "method": "Player.PlayPause",
    "params": {
      "playerid": int(player_id)
    },
    "id": "play_pause",
  }

def list_active_players():
  return {
    "jsonrpc": "2.0",
    "method": "Player.GetActivePlayers",
    "id": "list_active_players",
  }
