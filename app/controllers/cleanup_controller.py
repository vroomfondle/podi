from cement.core import controller
from lib.podi.rpc.library import clean_video_library, clean_audio_library
import argparse

class CleanupController(controller.CementBaseController):
  class Meta:
    label = 'cleanup'
    aliases = ['tidy']
    description = 'Clean up media libraries by removing non-existent items'
    stacked_on = 'base'
    stacked_type = 'nested'

  @controller.expose(hide=True)
  def default(self):
    self.app.log.info("Cleaning up video library")
    self.app.send_rpc_request(clean_video_library())
    self.app.log.info("Cleaning up audio library")
    self.app.send_rpc_request(clean_audio_library())


  
