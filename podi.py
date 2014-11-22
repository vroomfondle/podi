#!/usr/bin/env python
"""
A simple utility to list, play, pause and stop media files in XBMC/Kodi.
"""


from app import PodiApplication
from app.controllers import ListController, PlayController
from cement.core import handler


app = PodiApplication()
handler.register(ListController)
handler.register(PlayController)

try:
  app.setup()
  app.run()
finally:
  app.close()


