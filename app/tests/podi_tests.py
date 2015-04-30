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

"""
A few simple tests for Podi
"""
from unittest.mock import patch
from nose.tools import raises
from cement.utils import test
from app.podi_application import PodiApplication
from app.controllers import ListController, PlayController,\
    IntrospectController, PauseController, StopController,\
    CleanupController, UpdateController, InspectController,\
    ResumeController
from cement.core import handler
from app.errors import NoMediaError


class TestPodi(test.CementTestCase):
    app_class = PodiApplication

    def setUp(self):
        self.app = PodiApplication(argv=[])

    @patch('app.podi_application.PodiApplication.send_rpc_request')
    def test_podi_default(self, mock_sender):
        """Check that the app bootstraps without errors"""
        self.app.setup()
        self.app.run()
        self.app.close()

    @patch('app.podi_application.PodiApplication.send_rpc_request')
    def test_podi_list_shows(self, mock_sender):
        """
        Check that the 'list shows' function runs without errors
        and makes the correct RPC call. 
        """
        self.app = PodiApplication(argv=["list", "shows"])
        handler.register(ListController)
        self.app.setup()
        self.app.run()
        self.app.close()

        # at least one RPC call should have been made
        assert len(mock_sender.call_args) >= 1

        # check that the correct RPC method was called at least once
        shows_rpc_sent = False
        for call_args in mock_sender.call_args_list:
            if call_args[0][0]['method'] == 'VideoLibrary.GetTVShows':
                shows_rpc_sent = True
        assert shows_rpc_sent

    @patch('app.podi_application.PodiApplication.send_rpc_request')
    def test_podi_list_movies(self, mock_sender):
        """
        Check that the 'list movies' function runs without errors
        and makes the correct RPC call. 
        """
        self.app = PodiApplication(argv=["list", "movies"])
        handler.register(ListController)
        self.app.setup()
        self.app.run()
        self.app.close()

        # at least one RPC call should have been made
        assert len(mock_sender.call_args) >= 1

        # check that the correct RPC method was called at least once
        movies_rpc_sent = False
        for call_args in mock_sender.call_args_list:
            if call_args[0][0]['method'] == 'VideoLibrary.GetMovies':
                movies_rpc_sent = True
        assert movies_rpc_sent

    @patch('app.podi_application.PodiApplication.send_rpc_request')
    def test_podi_list_episodes(self, mock_sender):
        """
        Check that the 'list episodes' function runs without errors as long as
        at least one episode exists for the given show, and makes the correct
        RPC call.
        """
        mock_sender.return_value = {'episodes': [{'title':'test','runtime': 10,'episodeid':1}]}

        self.app = PodiApplication(argv=["list", "episodes", "1"])
        handler.register(ListController)
        self.app.setup()
        self.app.run()
        self.app.close()

        # at least one RPC call should have been made
        assert len(mock_sender.call_args) >= 1

        # check that the correct RPC method was called at least once
        episodes_rpc_sent = False
        for call_args in mock_sender.call_args_list:
            if call_args[0][0]['method'] == 'VideoLibrary.GetEpisodes':
                episodes_rpc_sent = True
        assert episodes_rpc_sent

    @raises(NoMediaError)
    @patch('app.podi_application.PodiApplication.send_rpc_request')
    def test_podi_list_episodes_none(self, mock_sender):
        """
        Check that the 'list episodes' function throws an error
        if no episodes exist for the given show
        """
        mock_sender.return_value = {}

        self.app = PodiApplication(argv=["list", "episodes", "1"])
        handler.register(ListController)
        self.app.setup()
        self.app.run()
        self.app.close()

        # at least one RPC call should have been made
        assert len(mock_sender.call_args) >= 1

        # check that the correct RPC method was called at least once
        episodes_rpc_sent = False
        for call_args in mock_sender.call_args_list:
            if call_args[0][0]['method'] == 'VideoLibrary.GetEpisodes':
                episodes_rpc_sent = True
        assert episodes_rpc_sent


    @patch('app.podi_application.PodiApplication.send_rpc_request')
    def test_podi_play_episode(self, mock_sender):
        self.app = PodiApplication(argv=["play", "episode", "1"])
        handler.register(PlayController)
        self.app.setup()
        self.app.run()
        self.app.close()

        # at least one RPC call should have been made
        assert len(mock_sender.call_args) >= 1

        # the most important RPC call is the one to Player.Open, so make sure that's been called
        # with the correct id
        player_opened = False
        correct_movie_id = False
        for call_args in mock_sender.call_args_list:
            if call_args[0][0]['method'] == 'Player.Open':
                player_opened = True
                assert call_args[0][0]['params']['item']['episodeid'] == 1
        assert player_opened

        
    @patch('app.podi_application.PodiApplication.send_rpc_request')
    def test_podi_play_movie(self, mock_sender):
        self.app = PodiApplication(argv=["play", "movie", "1"])
        handler.register(PlayController)
        self.app.setup()
        self.app.run()
        self.app.close()

        # at least one RPC call should have been made
        assert len(mock_sender.call_args) >= 1

        # the most important RPC call is the one to Player.Open, so make sure that's been called
        # with the correct id
        player_opened = False
        correct_movie_id = False
        for call_args in mock_sender.call_args_list:
            if call_args[0][0]['method'] == 'Player.Open':
                player_opened = True
                assert call_args[0][0]['params']['item']['movieid'] == 1
        assert player_opened

