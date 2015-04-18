#!/usr/bin/env python3
from CollectData import CollectData
from WebData import WebData
from HTMLComparison import HTMLComparison
import csv


__author__ = 'Jesse konstantindmitriev'


def main():
    collect = CollectData()
    number_of_webpages = 800
    list_of_urls = collect.get_list_of_first_n_urls_from_antizapret(number_of_webpages)
    list_of_urls_new = []
    # remove some urls
    for url in list_of_urls:
        if ('kupit' in url) or ('kuritelnye' in url) or ('kuritelnyy' in url) or ('pixiv' in url) or ('legalnye' in url) or ('jwh' in url) \
                or ('%' in url) or ('а' in url) or ('у' in url) or ('е' in url) or ('о' in url) or ('dumainet' in url) \
                or ('stopkid' in url) or ('kaktos' in url) or ('mnogo' in url) or ('nude' in url) or ('legal' in url) \
                or ('boy' in url) or ('porn' in url) or ('nerv' in url) or ('kupi' in url) or ('spice' in url)\
                or ('zakladki' in url) or ('spays' in url):
            pass
        else:
            list_of_urls_new.append(url)
    list_of_urls_dicts = []
    count = 50 if len(list_of_urls_new) > 50 else len(list_of_urls_new)
    for url in list_of_urls_new[:count]:
        list_of_urls_dicts = list_of_urls_dicts + [{'url': url}]

    list_of_urls_to_gather = list_of_urls_dicts
    for i in range(1, 50):
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

        # collect = CollectData()
        test_data = WebData()
        html_comparison = HTMLComparison()

        # number_of_webpages = 50
        blocking_country = 'Russia'

        # list of countries to explore
        countries = ['Finland', 'Estonia', 'Latvia', 'Lithuania', 'Belarus', 'Ukraine', 'Kazakhstan', 'Kyrgyzstan', 'Russia']
        # countries = ['Finland', 'Russia']#['Finland', 'Estonia', 'Latvia', 'Lithuania', 'Russia']

        for country in countries:
            print()
            collect.collect_multiple_webpages_from_single_country(
                country_id=country,
                number_of_webpages=number_of_webpages,
                use_manually_selected_list=False,
                test_data=test_data,
                list_of_urls_to_gather=list_of_urls_to_gather)

        session = False  # means current session
        # session = "2015-03-29_12-47-36"
        print()
        print('Analyzing...')
        dict_of_percentage_of_similarity = html_comparison.compare_files_between_countries(blocking_country, countries, test_data,
                                                                                    list_of_urls, session)

        # writing the results of the comparison
        w = csv.writer(open(test_data.getPathToSession() + "--output.csv", "w"))
        for country, urlAndPercentage in dict_of_percentage_of_similarity.items():
            w.writerow([country, urlAndPercentage])

        # # reading the results of the comparison
        # dict = {}
        # for country, urlAndPercentage in csv.reader(open(test_data.getPathToSession() + "--output.csv")):
        # dict[country] = urlAndPercentage

        print("\nDone")


if __name__ == '__main__':
    main()