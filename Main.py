#!/usr/bin/env python3
from CollectData import CollectData
from WebData import WebData
from HTMLComparison import HTMLComparison
import csv


__author__ = 'Jesse'


def main():
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
    test_data = WebData()
    html_comparison = HTMLComparison()

    number_of_webpages = 10
    blocking_country = 'Russia'

    # list of countries to explore
    # countries = ['Finland', 'Estonia', 'Latvia', 'Lithuania', 'Belarus', 'Ukraine', 'Kazakhstan', 'Kyrgyzstan', 'Russia']
    countries = ['Finland', 'Estonia', 'Russia']

    for country in countries:
        print()
        collect.collect_multiple_webpages_from_single_country(
            country_id=country,
            number_of_webpages=number_of_webpages,
            use_manually_selected_list=False,
            test_data=test_data)

    listOfURLs = collect.getListOfFirstNurlsFromAntiZapret(number_of_webpages)

    session = False  # means current session
    # session = "2015-03-29_12-47-36"

    dictOfPercentageOfSimilarity = html_comparison.compareFilesBetweenCountries(blocking_country, countries, test_data,
                                                                                listOfURLs, False)


    # writing the results of the comparison
    w = csv.writer(open(test_data.getPathToSession() + "--output.csv", "w"))
    for country, urlAndPercentage in dictOfPercentageOfSimilarity.items():
        w.writerow([country, urlAndPercentage])

    # # reading the results of the comparison
    # dict = {}
    # for country, urlAndPercentage in csv.reader(open(test_data.getPathToSession() + "--output.csv")):
    # dict[country] = urlAndPercentage

    print("\nDone")


if __name__ == '__main__':
    main()