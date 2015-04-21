#Podi


Podi is a command-line interface (CLI) program which can be used to control
the Kodi media player. It currently provides basic listing and playback 
functionality for movies and TV shows.

Movies, TV shows and TV episodes have a unique integer id within Kodi,
and this is displayed when listing media and used as a parameter when
playing things.

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
    podi --help

### Listing available media
    podi list movies
    podi list shows
    podi list episodes 133
### Playing media
    podi play movie 123
    podi play episode 255

