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

