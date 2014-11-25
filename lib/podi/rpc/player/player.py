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

def stop_player(player_id):
  return {
    "jsonrpc": "2.0",
    "method": "Player.Stop",
    "params": {
      "playerid": int(player_id)
    },
    "id": "stop",
  }


def list_active_players():
  return {
    "jsonrpc": "2.0",
    "method": "Player.GetActivePlayers",
    "id": "list_active_players",
  }


def inspect_player(player_id):
  return {
    "jsonrpc": "2.0",
    "method": "Player.GetProperties",
    "id": "player_properties",
    "params": {
        "playerid": int(player_id),
        "properties": [
          "percentage", "speed", "playlistid", "audiostreams", "position",
          "repeat", "currentsubtitle", "type", "subtitles", "canseek",
          "time", "totaltime", "currentaudiostream", "live", "subtitleenabled",
        ]
      }

  }


def inspect_current_item(player_id):
  return {
    "jsonrpc": "2.0",
    "method": "Player.GetItem",
    "id": "player_current_item",
    "params": {
      "playerid": int(player_id),
      "properties": [
        "file", "title", "originaltitle", "streamdetails", 
      ]
    }
  }


def enable_subtitles(player_id):
  return {
    "jsonrpc": "2.0",
    "method": "Player.SetSubtitle",
    "id": "set_subtitle",
    "params": {
      "playerid": int(player_id),
      "subtitle": "on",
    }
  }


def disable_subtitles(player_id):
  return {
    "jsonrpc": "2.0",
    "method": "Player.SetSubtitle",
    "id": "set_subtitle",
    "params": {
      "playerid": int(player_id),
      "subtitle": "off",
    }
  }


def select_subtitle(subtitle_id, player_id):
  return {
    "jsonrpc": "2.0",
    "method": "Player.SetSubtitle",
    "id": "set_subtitle",
    "params": {
      "playerid": int(player_id),
      "subtitle": int(subtitle_id),
    }
  }


def select_audio(audio_stream_id, player_id):
  return {
    "jsonrpc": "2.0",
    "method": "Player.SetAudioStream",
    "id": "set_subtitle",
    "params": {
      "playerid": int(player_id),
      "stream": int(audio_stream_id),
    }
  }
