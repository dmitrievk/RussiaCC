__author__ = 'tian'

"""
Connection package to VPNs under

Requirement
===========

1. Root privilege.
   You can run under command line interface using `sudo script.py`,
   or directly run IDE like PyCharm using sudo (not recommended)

2. Mac OS X
   Because the OpenVPN's up/down scripts differs, so only implementation for Mac OS X is done.


Components
=========

1. DirectConnection is a dummy connection doing nothing.
   It's for running code on local network.

2. OpenVPNConnection is the class with several parameters to control
   the running of OpenVPN.
   Don't use it unless one know how these parameter works


3. IPVanishConnection is a wrapper for OpenVPNConnection using configurations/credits from IPVanish.
   A directory named 'ipvanish-openvpn-configs' under project root.
   Inside following things are expected:

   1. several *.ovpn files.
      Their name should be consistent with 3rd column of ipVanish.txt
      They can be downloaded from IPVanish
   2. IPVanish credit file.
      A file named `ipvanishcredits.txt` with two lines: the first be username and the second be password
   3. up / down file.
      Two files can be extracted from tunnelblick from:
      * /Applications/Tunnelblick.app/Contents/Resources/client.up.tunnelblick.sh
      * /Applications/Tunnelblick.app/Contents/Resources/client.down.tunnelblick.sh

For each of the Connections, there are 3 method:
    1. __init__   --- the initializer
    2. connect()  --- try to connect.
       OpenVPNConnection and IPVanishConnection may raise OpenVPNException when calling connect()
       if it fails doing so, when network fails, or you're not root, or so.
    3. close()    --- close the connection. It's necessary.

Example
=======

To directly connect, the usage would be
    import Connection
    connection = Connection.DirectConnection()
    connection.connect()
    connection.close()

A three way usage is
    import Connection
    connection = Connection.IPVanishConnection('Finland')
    # Here 'Finland' can be any country in file ipVanish.txt
    connection.connect()
    connection.close()

An concrete example would be

    import Connection
    print('IP before using VPN', Connection.get_ip())
    connection = Connection.IPVanishConnection('Finland')
    print('connecting...')
    connection.connect()
    print('connected')
    print('IP while using VPN', Connection.get_ip())
    connection.close()
    print('closed')
    print('IP after using VPN', Connection.get_ip())
"""

from .Connection import Connection
from .DirectConnection import DirectConnection
from .OpenVPNConnection import OpenVPNConnection, OpenVPNException
from .IPVanishConnection import IPVanishConnection, IPVanishException, NoSuchCountryException
from .Util import get_ip
