#!/usr/bin/env python3
from CollectData import CollectData
from WebData import WebData


__author__ = 'Jesse'

print("Starting RussiaCC\n")

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

# list of countries to explore
countries = ['Finland', 'Estonia', 'Latvia', 'Lithuania', 'Belarus', 'Ukraine', 'Kazakhstan', 'Kyrgyzstan', 'Russia']

for country in countries:
    print()
    collect.collectMultipleWebpagesFromASingleCountry(country, 10, False, testData)


print("\nDone")

