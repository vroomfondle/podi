from cement.core import controller
from lib.podi.rpc.library import update_video_library, update_audio_library
import argparse

class UpdateController(controller.CementBaseController):
  class Meta:
    label = 'update'
    aliases = ['scan']
    description = 'Update media libraries by scanning for new files'
    stacked_on = 'base'
    stacked_type = 'nested'

  @controller.expose(hide=True)
  def default(self):
    self.app.log.info("Updating videos")
    self.app.send_rpc_request(update_video_library())
    self.app.log.info("Updating audio")
    self.app.send_rpc_request(update_audio_library())


  
