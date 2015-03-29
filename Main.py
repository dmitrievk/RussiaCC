#!/usr/bin/env python3
from CollectData import CollectData
from WebData import WebData
from HTMLComparison import HTMLComparison
import csv


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
htmlComparison = HTMLComparison()

numberOfWebPagesToAccess = 10
blockingCountry = 'Russia'

# list of countries to explore
# countries = ['Finland', 'Estonia', 'Latvia', 'Lithuania', 'Belarus', 'Ukraine', 'Kazakhstan', 'Kyrgyzstan', 'Russia']
countries = ['Finland', 'Estonia', 'Russia']

for country in countries:
    print()
    collect.collectMultipleWebpagesFromASingleCountry(country, numberOfWebPagesToAccess, False, testData)

listOfURLs = collect.getListOfFirstNurlsFromAntiZapret(numberOfWebPagesToAccess)

session = False  # means current session
# session = "2015-03-29_12-47-36"

dictOfPercentageOfSimilarity = htmlComparison.compareFilesBetweenCountries(blockingCountry, countries, testData, listOfURLs, False)


# writing the results of the comparison
w = csv.writer(open(testData.getPathToSession() + "--output.csv", "w"))
for country, urlAndPercentage in dictOfPercentageOfSimilarity.items():
    w.writerow([country, urlAndPercentage])

# # reading the results of the comparison
# dict = {}
# for country, urlAndPercentage in csv.reader(open(testData.getPathToSession() + "--output.csv")):
#     dict[country] = urlAndPercentage

print("\nDone")

