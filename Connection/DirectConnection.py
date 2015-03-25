__author__ = 'tian'

from .Connection import Connection


class DirectConnection(Connection):
    """
    Direct connection (without using any VPN)
    """

    def connect(self):
        pass

    def close(self):
        pass
