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
from .list_controller import ListController
from .play_controller import PlayController
from .resume_controller import ResumeController
from .introspect_controller import IntrospectController
from .pause_controller import PauseController
from .stop_controller import StopController
from .cleanup_controller import CleanupController
from .update_controller import UpdateController
from .inspect_controller import InspectController
