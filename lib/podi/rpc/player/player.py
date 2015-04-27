"""
    Podi, a command-line interface for Kodi.
    Copyright (C) 2015  Peter Frost <slimeypete@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


def play_file(file_path, resume=False):
    """
    :returns A dict representing the JSON RPC call to play a file.
    :param file_path The full path to the file.
    :param resume If true, the file will be resumed from the last known time. Default is False.
    """

    return {
        "jsonrpc": "2.0",
        "method": "Player.Open",
        "params": {
            "item": {"file": file_path},
            "options": {"resume": bool(resume)},
        },
        "id": "play_file"
    }


def play_movie(movie_id, resume=False):
    """
    :returns A dict representing the JSON RPC call to play a movie by id.
    :param file_path The id of the movie.
    :param resume If true, the movie will be resumed from the last known time. Default is False.
    """
    return {
        "jsonrpc": "2.0",
        "method": "Player.Open",
        "params": {
            "item": {"movieid": int(movie_id)},
            "options": {"resume": bool(resume)},
        },
        "id": "play_movie_{0}".format(movie_id)
    }


def play_episode(episode_id, resume=False):
    """
    :returns A dict representing the JSON RPC call to play a TV show episode by id.
    :param file_path The id of the movie.
    :param resume If true, the episode will be resumed from the last known time. Default is False.
    """
    return {
        "jsonrpc": "2.0",
        "method": "Player.Open",
        "params": {
            "item": {"episodeid": int(episode_id)},
            "options": {"resume": bool(resume)},
        },
        "id": "play_tv_episode_{0}".format(episode_id)
    }


def pause_unpause_player(player_id):
    """
    :returns A dict representing the JSON RPC call to pause or unpause the media player.
    :param file_path The id of the player which is to be paused or unpaused.
    """
    return {
        "jsonrpc": "2.0",
        "method": "Player.PlayPause",
        "params": {
            "playerid": int(player_id)
        },
        "id": "play_pause",
    }


def stop_player(player_id):
    """
    :returns A dict representing the JSON RPC call to stop playback via the given media player.
    :param file_path The id of the player which is to be stopped.
    """
    return {
        "jsonrpc": "2.0",
        "method": "Player.Stop",
        "params": {
            "playerid": int(player_id)
        },
        "id": "stop",
    }


def list_active_players():
    """
    :returns A dict representing the JSON RPC call to list active media players.
    """

    return {
        "jsonrpc": "2.0",
        "method": "Player.GetActivePlayers",
        "id": "list_active_players",
    }


def inspect_player(player_id):
    """
    :returns A dict representing the JSON RPC call to retrieve details of the given media player.
    :param player_id The id of the player to be inspected.
    """

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
    """
    :returns A dict representing the JSON RPC call to retrieve details of the media item
        which is being played by the given player.
    :param player_id The id of the player to be inspected.
    """

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
    """
    :returns A dict representing the JSON RPC call to enable subtitle playback by the given media player.
    :param player_id The id of the player which is to start displaying subtitles.
    """

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
    """
    :returns A dict representing the JSON RPC call to disable subtitle playback by the given media player.
    :param player_id The id of the player which is to stop displaying subtitles.
    """

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
    """
    :returns A dict representing the JSON RPC call to tell the given media player to
        switch to the given subtitle track.
    :param player_id The id of the player which is to display the subtitles.
    :param subtitle_id The id of the subtitle track to be used.
    """

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
    """
    :returns A dict representing the JSON RPC call to tell the given media player to
        switch to the given audio track.
    :param player_id The id of the player which is to display the audios.
    :param audio_id The id of the audio track to be used.
    """

    return {
        "jsonrpc": "2.0",
        "method": "Player.SetAudioStream",
        "id": "set_subtitle",
        "params": {
            "playerid": int(player_id),
            "stream": int(audio_stream_id),
        }
    }
