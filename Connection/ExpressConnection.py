__author__ = 'jessebrizzi'


import os
from os.path import dirname, realpath, join
from .Connection import Connection
from .OpenVPNConnection import OpenVPNConnection


class ExpressException(OpenVPNConnection):
    pass


class NoSuchCountryException(ExpressException):
    pass


class ExpressConnection(OpenVPNConnection):
    def __init__(self, country, **kwargs):
        project_dir = join(dirname(realpath(__file__)), '..')
        express_dir = join(project_dir, 'express-openvpn-configs')
        express_mapping_file = join(project_dir, 'express.txt')

        mapping = dict()
        for line in open(express_mapping_file):
            tokens = line.strip('\r\n').split(',')
            _country, config = tokens[0], tokens[2]
            mapping[_country] = config

        if country not in mapping:
            raise NoSuchCountryException({'Country Provided': country,
                                          'Countries Available': mapping.keys()})

        super().__init__(cd=express_dir,
                         auth=join(express_dir, 'ipvanishcredits.txt'),
                         config=join(express_dir, mapping[country]),
                         management_port=1337,
                         up_script='"%s%s"' % (
                         join(express_dir, 'client.up.tunnelblick.sh'), ' -d -f -m -w -ptADGNWradsgnw'),
                         down_script='"%s%s"' % (
                         join(express_dir, 'client.down.tunnelblick.sh'), ' -d -f -m -w -ptADGNWradsgnw'))
