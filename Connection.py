#!/usr/bin/env python3


class Connection:
    """
    Base class for a connection
    It should not be used directly
    """

    def __init__(self):
        pass

    def connect(self):
        raise NotImplemented

    def close(self):
        raise NotImplemented


class DirectConnection(Connection):
    """
    Direct connection (without using any VPN)
    """

    def connect(self):
        pass

    def close(self):
        pass


class OpenVPNConnection(Connection):
    def __init__(config_path):
        super().__init__()
        
        pass

    def connect(self):
        pass

    def close(self):
        pass
