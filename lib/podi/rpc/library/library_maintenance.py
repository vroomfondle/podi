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


def clean_video_library():
    """
    :returns A dict representing the JSON RPC call to tell Kodi to clean up its video library
        (remove missing files etc.)
    """

    return {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.Clean",
        "id": "clean_video_library",
    }


def clean_audio_library():
    """
    :returns A dict representing the JSON RPC call to tell Kodi to clean up its audio library
        (remove missing files etc.)
    """

    return {
        "jsonrpc": "2.0",
        "method": "AudioLibrary.Clean",
        "id": "clean_audio_library",
    }


def update_video_library():
    """
    :returns A dict representing the JSON RPC call to tell Kodi to update its video library
        (add new files etc.)
    """

    return {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.Scan",
        "id": "scan_video_library",
    }


def update_audio_library():
    """
    :returns A dict representing the JSON RPC call to tell Kodi to update its audio library
        (add new files etc.)
    """

    return {
        "jsonrpc": "2.0",
        "method": "AudioLibrary.Scan",
        "id": "scan_audio_library",
    }
