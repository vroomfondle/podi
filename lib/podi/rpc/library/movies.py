"""
    Defines functions which will generate dicts representing JSON RPC calls to interact with Kodi
    regarding movies.

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


def list_movies(filters=None):
    """
    :returns A dict representing the JSON RPC call to retrieve a list of movies from Kodi's library.
    """

    request = {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetMovies",
        "id": "list_movies",
        "params": {
            "properties": [
                "file", "title", "originaltitle",
                "genre", "year", "tag",
                "director", "studio", "cast", "imdbnumber",
                "mpaa", "playcount", "rating",
                "runtime", "set", "showlink", "top250",
                "votes", "sorttitle", "resume", "setid", "dateadded",
                "streamdetails",
            ],
        },
    }

    if filters is not None and len(filters) != 0:
        request['params']['filter'] = []
        for index in range(len(filters)):
            request['params']['filter'].append(
                {list(filters[0].keys())[0]: list(filters[0].values())[0], }
            )

    return request


def inspect_movie(movie_id):
    """
    :returns A dict representing the JSON RPC call to retrieve details of a specific movie in Kodi's library.
    :param movie_id The id of the movie to be inspected.
    """

    return {
        "jsonrpc": "2.0",
        "method": "VideoLibrary.GetMovieDetails",
        "id": "movie_details",
        "params": {
            "movieid": int(movie_id),
            "properties": [
                "file", "title", "originaltitle",
                "genre", "year", "tag", "tagline", "writer",
                "director", "studio", "cast", "imdbnumber", "country",
                "mpaa", "playcount", "rating", "plot", "plotoutline",
                "runtime", "set", "showlink", "streamdetails", "top250",
                "votes", "sorttitle", "resume", "setid", "dateadded",
            ],
        },
    }
