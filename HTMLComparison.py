__author__ = 'konstantindmitriev'

from difflib import SequenceMatcher
from WebData import WebData

class HTMLComparison:

    def __init__(self):
        pass

    # compares gathered files between countries and blockingCountry
    # from either current session (session = False) or a particular session (e.g. session = "2015-03-29_12-47-36")
    # returns dictionary: key - country, value - [{url1: difference1 in %}, {url2: difference2 in %} ...]
    def compare_files_between_countries(self, blocking_country, countries, test_data, list_of_urls, session):  #blockingCountry = Russia
        dict_of_percentage_of_similarity = {}  # key - country, value - [{url1: difference1 in %}, {url2: difference2 in %} ...]
        countries.remove(blocking_country)
        for country in countries:
            dict_of_percentage_of_similarity[country] = []


        if session:
                test_data.setSession(session)

        for url in list_of_urls:
            dict_of_webpages_from_different_vpn_servers = test_data.get_all_webpages(url)  # keys are the vpn names
            page_from_blocking_country = dict_of_webpages_from_different_vpn_servers[blocking_country]
            del dict_of_webpages_from_different_vpn_servers[blocking_country]

            for country in dict_of_webpages_from_different_vpn_servers.keys():
                page_from_current_country = dict_of_webpages_from_different_vpn_servers[country]
                percentage_of_difference = self.compare_two_html_files(page_from_blocking_country,
                                                                    page_from_current_country)
                tempList = dict_of_percentage_of_similarity[country]
                tempList.append({url: percentage_of_difference})
                dict_of_percentage_of_similarity[country] = tempList  # dict_of_percentage_of_similarity.update({url: percentage_of_difference})

        return dict_of_percentage_of_similarity

    # compares two html files and returns percent of similarity
    def compare_two_html_files(self, html1, html2):
        similarity = SequenceMatcher(None, html1, html2)

        return similarity.ratio()*100