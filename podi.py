#!/usr/bin/env python
"""
A simple utility to list, play, pause and stop media files in XBMC/Kodi.
"""
from httplib import HTTPConnection
from urllib import quote



host="192.168.1.147"
port=8080
jsonRPCReq = '{ "jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1 }'
headers={"Content-type": "application/json"}

conn = HTTPConnection(host, port)
conn.request("GET", "/jsonrpc?request=%s" % quote(jsonRPCReq, ''), None, headers)

print conn.getresponse().read()

