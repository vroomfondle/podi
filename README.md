#Podi


Podi is a command-line interface (CLI) program which can be used to control
the Kodi media player. It currently provides basic listing and playback 
functionality for movies and TV shows.

Movies, TV shows and TV episodes have a unique integer id within Kodi,
and this is displayed when listing media and used as a parameter when
playing things.

##Requirements
Podi requires Python 3 and a version of Kodi which implements version 6
of the Kodi JSON-RPC API (Kodi 13.0 onwards).

##Configuring Kodi
You need to enable the Kodi web interface before you can use Podi.
See http://kodi.wiki/view/Web_interface

##Configuration
Put the following in $HOME/podi.conf, subsituting values
as necessary to represent your Kodi web interface details.


    [Configuration]
    host=192.168.1.176
    port=8080
    user=xbmc
    password=


##Usage
    ./podi.py --help

### Listing available media
    ./podi.py list movies
    ./podi.py list shows
    ./podi.py list episodes 133
### Playing media
    ./podi.py play movie 123
    ./podi.py play episode 255


