__author__ = 'tian'

import os
from os.path import dirname, realpath, join
from .Connection import Connection
from .OpenVPNConnection import OpenVPNConnection


class IPVanishException(OpenVPNConnection):
    pass


class NoSuchCountryException(IPVanishException):
    pass


class IPVanishConnection(OpenVPNConnection):
    def __init__(self, country, **kwargs):
        project_dir = join(dirname(realpath(__file__)), '..')
        ipvanish_dir = join(project_dir, 'ipvanish-openvpn-configs')
        ipvanish_mapping_file = join(project_dir, 'ipVanish.txt')

        mapping = dict()
        for line in open(ipvanish_mapping_file):
            tokens = line.strip('\r\n').split(',')
            _country, config = tokens[0], tokens[2]
            mapping[_country] = config

        if country not in mapping:
            raise NoSuchCountryException({'Country Provided': country,
                                          'Countries Available': mapping.keys()})

        super().__init__(cd=ipvanish_dir,
                         auth=join(ipvanish_dir, 'ipvanishcredits.txt'),
                         config=join(ipvanish_dir, mapping[country]),
                         management_port=1337,
                         up_script='"%s%s"' % (
                         join(ipvanish_dir, 'client.up.tunnelblick.sh'), ' -d -f -m -w -ptADGNWradsgnw'),
                         down_script='"%s%s"' % (
                         join(ipvanish_dir, 'client.down.tunnelblick.sh'), ' -d -f -m -w -ptADGNWradsgnw'))
