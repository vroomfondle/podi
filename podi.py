#!/usr/bin/env python3
"""
A simple utility to list, play, pause and stop media files in XBMC/Kodi.


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


from app import PodiApplication
from app.controllers import ListController, PlayController,\
    IntrospectController, PauseController, StopController,\
    CleanupController, UpdateController, InspectController,\
    ResumeController
from cement.core import handler


if __name__ == '__main__':
    app = PodiApplication()
    handler.register(CleanupController)
    handler.register(IntrospectController)
    handler.register(InspectController)
    handler.register(ListController)
    handler.register(PlayController)
    handler.register(PauseController)
    handler.register(StopController)
    handler.register(UpdateController)
    handler.register(ResumeController)

    try:
        app.setup()
        app.run()
    finally:
        app.close()
