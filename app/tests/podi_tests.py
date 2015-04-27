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
