#!/usr/bin/env python3
"""
A simple utility to list, play, pause and stop media files in XBMC/Kodi.
"""


from app import PodiApplication
from app.controllers import ListController, PlayController, IntrospectController
from app.controllers import PauseController, StopController, CleanupController
from app.controllers import UpdateController, InspectController, ResumeController
from cement.core import handler


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


