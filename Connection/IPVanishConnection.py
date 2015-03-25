__author__ = 'tian'

import os
from .Connection import Connection
from .OpenVPNConnection import OpenVPNConnection


class IPVanishConnection(OpenVPNConnection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



    pass