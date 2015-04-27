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
from cement.core import controller
from lib.podi.rpc.library import inspect_movie, inspect_episode,\
    inspect_tv_show
from lib.podi.rpc.player import inspect_player, list_active_players, inspect_current_item
from lib.podi.util import retrieve_sorted_episodes, list_to_dicts
from app.errors import JSONResponseError
import argparse


class InspectController(controller.CementBaseController):
    """
    Sends RPC calls to Kodi to retrieve details about media items or media players.
    """

    class Meta:
        """
        Defines controller metadata for the Cement framework to pick up.
        """

        label = 'inspect'
        description = 'Retrieve and display inspects of media items'
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [(['positional_arguments'], dict(
            action='store', nargs='*', help=argparse.SUPPRESS),), ]

    @controller.expose(hide=True)
    def default(self):
        """
        Prints the help text when no arguments have been specified.
        """

        self.app.args.print_help()

    @controller.expose(
        aliases=['film'],
        help='Show information about a movie. Provide the id number of the movie (e.g. inspect movie 107).')
    def movie(self):
        """
        Inspects a movie.
        """

        try:
            movie_id = self.app.pargs.positional_arguments[0]
        except IndexError as err:
            self.app.log.error("You must provide a movie id number")
            return False
        try:
            movie_details = self.app.send_rpc_request(
                inspect_movie(movie_id))['moviedetails']
        except JSONResponseError as err:
            if err.error_code == -32602:
                self.app.log.error(
                    "Kodi returned an 'invalid parameters' error; this movie may not exist?")
                return False
            else:
                raise err
        list_to_dicts(key='tag', input_list=movie_details['tag'])
        list_to_dicts(key='genre', input_list=movie_details['genre'])
        list_to_dicts(key='writer', input_list=movie_details['writer'])
        list_to_dicts(key='country', input_list=movie_details['country'])
        print(self.app.render(movie_details, 'movie_details.m', None))

    @controller.expose(aliases=['tv_show', 'tv', 'tvshow'],
                       help='Show information about a TV show. Provide the id number of the show (e.g. inspect show 9).')
    def show(self):
        """
        Inspects a TV show.
        """

        try:
            tv_show_id = self.app.pargs.positional_arguments[0]
        except IndexError as err:
            self.app.log.error("You must provide a show id number")
            return False
        try:
            tv_show_details = self.app.send_rpc_request(
                inspect_tv_show(tv_show_id))['tvshowdetails']
        except JSONResponseError as err:
            if err.error_code == -32602:
                self.app.log.error(
                    "Kodi returned an 'invalid parameters' error; this tv_show may not exist?")
                return False
            else:
                raise err
        list_to_dicts(key='tag', input_list=tv_show_details['tag'])
        list_to_dicts(key='genre', input_list=tv_show_details['genre'])
        tv_show_details['episodes'] = retrieve_sorted_episodes(
            self.app.send_rpc_request, tv_show_id)
        print(self.app.render(tv_show_details, 'tv_show_details.m', None))

    @controller.expose(aliases=['tv_episode', 'tvepisode'],
                       help='Show information about a TV show episode. Provide an episode id number (e.g. inspect episode 155).')
    def episode(self):
        """
        Inspects a TV episode.
        """

        try:
            episode_id = self.app.pargs.positional_arguments[0]
        except IndexError as err:
            self.app.log.error("You must provide a episode id number")
            return False
        try:
            episode_details = self.app.send_rpc_request(
                inspect_episode(episode_id))['episodedetails']
        except JSONResponseError as err:
            if err.error_code == -32602:
                self.app.log.error(
                    "Kodi returned an 'invalid parameters' error; this episode may not exist?")
                return False
            else:
                raise err
        list_to_dicts(key='writer', input_list=episode_details['writer'])
        print(self.app.render(episode_details, 'episode_details.m', None))

    @controller.expose(
        help='Show information about the currently-active media player, including available audio and subtitle streams.')
    def player(self):
        """
        Inspects a media player.
        """

        for player in self.app.send_rpc_request(list_active_players()):
            player_details = self.app.send_rpc_request(
                inspect_player(player['playerid']))
            player_details['repeat'] = (player_details['repeat'] == 'on')
            self.app.log.debug(player_details)
            player_details['item'] = self.app.send_rpc_request(
                inspect_current_item(player['playerid']))['item']
            print(self.app.render(player_details, 'player_details.m', None))
