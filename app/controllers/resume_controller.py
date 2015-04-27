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
from lib.podi.rpc.library.movies import list_movies
from lib.podi.rpc.player import play_episode, play_movie
from app.errors import JSONResponseError
import argparse


class ResumeController(controller.CementBaseController):
    """
    Sends RPC calls to instruct Kodi to resume playback of media items.
    """

    class Meta:
        """
        Defines metadata for use by the Cement framework.
        """

        label = 'resume'
        description = 'Resume playback of a given media item (or play it from the start if not resumable).'
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [(['positional_arguments'], dict(
            action='store', nargs='*', help=argparse.SUPPRESS),), ]

    @controller.expose(hide=True)
    def default(self):
        """
        Prints the help text when the user has supplied no arguments.
        """

        self.app.args.print_help()

    @controller.expose(
        aliases=[
            'movies',
            'film',
            'films'],
        help="Play a movie, resuming at the last-watched timestamp if possible. "\
            "You must provide a movie id number, e.g.: resume movie 127")
    def movie(self):
        """
        Instructs Kodi to resume playback of the movie specified by the user.
        """

        try:
            movie_id = self.app.pargs.positional_arguments[0]
        except IndexError as err:
            self.app.log.error(
                'You must provide a movie id number, e.g.: play movie 127')
            return False

        try:
            movie = [movie_details for movie_details in self.app.send_rpc_request(list_movies())['movies']
                     if str(movie_details['movieid']) == movie_id][0]
        except IndexError as err:
            self.app.log.error("Movie {0} not found.".format(movie_id))
            return False
        self.app.log.info(
            "Playing/resuming movie {0}: {1} ({2})".format(movie_id, movie['label'], movie['file']))
        self.app.send_rpc_request(play_movie(movie_id=movie_id, resume=True))

    @controller.expose(
        aliases=[
            'tvepisode',
            'tv_episode'],
        help="Play a TV episode, resuming at the last-watched timestamp if possible. "\
        "You must provide an episode id number, e.g.: resume episode 1340")
    def episode(self):
        """
        Instructs Kodi to resume playback of the TV episode specified by the user.
        """

        try:
            episode_id = self.app.pargs.positional_arguments[0]
        except IndexError as err:
            self.app.log.error(
                'You must provide an episode id number, e.g.: play movie 127')
            return False
        self.app.log.info("Playing/resuming episode {0}".format(episode_id))
        try:
            self.app.send_rpc_request(
                play_episode(episode_id=episode_id, resume=True))
        except JSONResponseError as err:
            if err.error_code == -32602:
                self.app.log.error(
                    "Kodi returned an 'invalid parameters' error; this episode may not exist? "\
                    "Use 'list episodes' to  see available episodes.")
                return False
            else:
                raise err
