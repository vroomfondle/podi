#!/usr/bin/env python3

"""
A few simple tests for Podi
"""
from cement.utils import test
from app.podi_application import PodiApplication
from app.controllers import ListController, PlayController,\
  IntrospectController, PauseController, StopController,\
  CleanupController, UpdateController, InspectController,\
  ResumeController
from cement.core import handler



class FakePodi(PodiApplication):
  class Meta:
    argv = []

class TestPodi(test.CementTestCase):
  app_class = FakePodi

  def test_podi_default(self):
    """Check that the app bootstraps without errors"""
    self.app.setup()
    self.app.run()
    self.app.close()

  def test_podi_list_shows(self):
    """Check that the 'list shows' function runs without errors"""
    self.app = FakePodi(argv=["list", "shows"])
    handler.register(ListController)
    self.app.setup()
    self.app.run()
    self.app.close()

  def test_podi_list_movies(self):
    """Check that the 'list movies' function runs without errors"""
    self.app = FakePodi(argv=["list", "movies"])
    handler.register(ListController)
    self.app.setup()
    self.app.run()
    self.app.close()


  def test_podi_list_episodes(self):
    """Check that the 'list episodes' function runs without errors"""
    self.app = FakePodi(argv=["list", "episodes", "1"])
    handler.register(ListController)
    self.app.setup()
    self.app.run()
    self.app.close()
