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
from lib.podi.rpc.player import play_movie, play_episode,\
    enable_subtitles, select_subtitle, list_active_players, select_audio, pause_unpause_player
from app.errors import JSONResponseError, NoMediaError, MissingArgumentError
import argparse


class PlayController(controller.CementBaseController):
    """
    Sends RPC calls to Kodi to request playback of media items.
    """

    class Meta:
        """
        Defines metadata for use by the Cement framework.
        """

        label = 'play'
        description = "Trigger playback of a given media item "\
                      "(if no item is specified, any currently-playing media items will be paused or unpaused)."
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [(['positional_arguments'], dict(
            action='store', nargs='*', help=argparse.SUPPRESS),), ]

    @controller.expose(hide=True)
    def default(self):
        """
        Called when the user uses the 'play' command without arguments. Requests resumption of playback
        of the current media item.
        """

        players = self.app.send_rpc_request(list_active_players())
        for player in players:
            self.app.log.info("Pausing/unpausing {0}".format(player['type']))
            self.app.send_rpc_request(pause_unpause_player(player['playerid']))
        if len(players) == 0:
            raise MissingArgumentError(
                "No media item was specified for playback, and there are no currently-playing media items to pause/unpause.")

    @controller.expose(aliases=['movies', 'film', 'films'],
                       help='Play a movie. You must provide a movie id number, e.g.: play movie 127')
    def movie(self):
        """
        Instructs Kodi to play the movie specified by the user.
        """

        try:
            movie_id = self.app.pargs.positional_arguments[0]
        except IndexError:
            raise MissingArgumentError(
                'You must provide a movie id number, e.g.: play movie 127')

        self.app.log.info("Playing movie {0}".format(
            movie_id))
        try:
            self.app.send_rpc_request(play_movie(movie_id))
        except JSONResponseError as err:
            if err.error_code == -32602:
                raise NoMediaError(
                    "Kodi returned an 'invalid parameters' error; this movie may not exist? "
                    "Use 'list episodes' to  see available episodes.")
            else:
                raise err

    @controller.expose(aliases=['tvepisode', 'tv_episode'],
                       help='Play a TV episode. You must provide an episode id number, e.g.: play episode 1340')
    def episode(self):
        """
        Instructs Kodi to play the TV episode specified by the user.
        """

        try:
            tv_episode_id = self.app.pargs.positional_arguments[0]
        except IndexError as err:
            raise MissingArgumentError(
                'You must provide an episode id number, e.g.: play movie 127')
        self.app.log.info("Playing episode {0}".format(tv_episode_id))
        try:
            self.app.send_rpc_request(play_episode(tv_episode_id))
        except JSONResponseError as err:
            if err.error_code == -32602:
                raise NoMediaError(
                    "Kodi returned an 'invalid parameters' error; this episode may not exist? "
                    "Use 'list episodes' to  see available episodes.")
            else:
                raise err

    @controller.expose(
        aliases=['subtitles'],
        help="Show subtitles. You must provide a subtitle stream id (e.g. play subtitles 2). Use "\
            "\"inspect player\" to see a list of available streams.")
    def subtitle(self):
        """
        Instructs Kodi to display the subtitle track specified by the user.
        """

        try:
            subtitle_id = self.app.pargs.positional_arguments[0]
        except IndexError as err:
            raise MissingArgumentError(
                "You must provide a subtitle id number, e.g.: play subtitle 2. Use \"inspect player\""
                " to see a list of available subtitle streams.")
        for player in self.app.send_rpc_request(list_active_players()):
            try:
                self.app.send_rpc_request(enable_subtitles(player['playerid']))
                self.app.send_rpc_request(
                    select_subtitle(subtitle_id, player['playerid']))
            except JSONResponseError as err:
                if err.error_code == -32602:
                   raise NoMediaError(
                        "Kodi returned an 'invalid parameters' error; this stream may not exist? Use "
                        "\"inspect player\" to see a list of available streams.")
                else:
                    raise err

    @controller.expose(
        aliases=['audio_stream'],
        help="Select an audio stream for the currently-playing video. You must provide a audio stream "\
            "id (e.g. play audio 2). Use \"inspect player\" to see a list of available audio streams.")
    def audio(self):
        """
        Instructs Kodi to play the audio track specified by the user.
        """

        try:
            audio_id = self.app.pargs.positional_arguments[0]
        except IndexError as err:
            raise MissingArgumentError(
                "You must provide a audio id number, e.g.: play audio 2. Use \"inspect player\" to see "
                "a list of available audio streams.")
        for player in self.app.send_rpc_request(list_active_players()):
            try:
                self.app.send_rpc_request(
                    select_audio(audio_id, player['playerid']))
            except JSONResponseError as err:
                if err.error_code == -32602:
                    raise NoMediaError(
                        "Kodi returned an 'invalid parameters' error; this stream may not exist? Use "
                        "\"inspect player\" to see a list of available streams.")
                else:
                    raise err
