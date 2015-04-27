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
from .library_maintenance import clean_audio_library
from .library_maintenance import clean_video_library
from .library_maintenance import update_audio_library
from .library_maintenance import update_video_library
from .tv_shows import list_tv_shows
from .tv_shows import list_episodes
from .movies import list_movies
from .movies import inspect_movie
from .tv_shows import inspect_tv_show
from .tv_shows import inspect_episode
