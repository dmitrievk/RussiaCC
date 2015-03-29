#!/usr/bin/env python3
from CollectData import CollectData
from WebData import WebData


__author__ = 'Jesse'

print("hello world")

# An example to use Connection
# import Connection
#
# print('IP before using VPN', Connection.get_ip())
# connection = Connection.IPVanishConnection('Finland')
# print('connecting...')
# connection.connect()
# print('connected')
# print('IP while using VPN', Connection.get_ip())
# connection.close()
# print('closed')
# print('IP after using VPN', Connection.get_ip())

collect = CollectData()
testData = WebData()

collect.collectMultipleWebpagesFromASingleCountry('Finland', 10, False, testData)


