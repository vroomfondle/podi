#!/usr/bin/env python
"""
A simple utility to list, play, pause and stop media files in XBMC/Kodi.
"""


from app import PodiApplication
from app.controllers import ListController, PlayController, IntrospectController, PauseController, StopController
from cement.core import handler


app = PodiApplication()
handler.register(ListController)
handler.register(PlayController)
handler.register(PauseController)
handler.register(StopController)
handler.register(IntrospectController)

try:
  app.setup()
  app.run()
finally:
  app.close()


