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
from .player import play_file
from .player import play_movie
from .player import play_episode
from .player import pause_unpause_player
from .player import list_active_players
from .player import stop_player
from .player import inspect_player
from .player import inspect_current_item
from .player import select_audio
from .player import select_subtitle
from .player import enable_subtitles
from .player import disable_subtitles
