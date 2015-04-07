__author__ = 'konstantindmitriev JesseBrizzi'

# download and install requests "pip3 install requests"
import requests
import json
from WebData import WebData
import Connection


class CollectData:
    # Russian providers do not block every page from the register
    # This is the list of manually selected pages that cannot be accessed from the russian VPN server (IPVanish)
    # but they are accessible from the servers outside of Russia
    list_of_definitely_blocked_pages = [{'url': 'http://leonwolf.livejournal.com', 'ip': '208.93.0.190'},
                                    {'url': 'http://navalny.livejournal.com', 'ip': '208.93.0.190'},
                                    {'url': 'https://twitter.com/b0ltai', 'ip': 'idk'}]

    def __init__(self):
        # Init Connection Class
        # self.connection = Connection()
        # Init SaveData Class
        pass

    # access multiple webpages from a single country
    def collect_multiple_webpages_from_single_country(self,
                                                  country_id = None,
                                                  number_of_webpages = -1,
                                                  use_manually_selected_list = False,
                                                  test_data = None
    ):
        # open the connection using countryID
        print('IP before using VPN', Connection.get_ip())

        # if country_id is not None:
        #     connection = Connection.IPVanishConnection(country_id)
        # else:
        #     connection = Connection.DirectConnection()
        #     country_id = 'SampleCountry'

        connection = Connection.DirectConnection()

        print('connecting...')
        connection.connect()
        print('connected to ' + country_id)
        print('IP while using VPN', Connection.get_ip())

        # list_of_blocked_websites = []
        if use_manually_selected_list:
            list_of_blocked_websites = self.list_of_definitely_blocked_pages
        else:
            request_a_list_of_blocked_websites = requests.get('http://api.antizapret.info/all.php?type=json')
            # decode the received data
            list_of_blocked_websites = json.loads(request_a_list_of_blocked_websites.text)['register']
        # go through websites in the list
        for blocked_website in list_of_blocked_websites[:number_of_webpages]:  # first n results
            blocked_url = blocked_website['url']
            html_code_of_the_page = requests.get(blocked_url, timeout=8).text  # timeout = 8 seconds

            if html_code_of_the_page == '':
                html_code_of_the_page = "None"
            # print(blocked_url)
            # print(html_code_of_the_page)

            # save html code of the page (input: blocked_url, html_code_of_the_page)
            test_data.save_webpage(html_code_of_the_page, blocked_url, country_id)

        # close the connection
        connection.close()
        print('closed')
        print('IP after using VPN', Connection.get_ip())

    # access a single webpage from multiple countries
    def collect_one_webpage_from_multiple_coutries(self, list_of_country_ids, url, test_data):
        for country_id in list_of_country_ids:
            # open the connection using country_id
            print('IP before using VPN', Connection.get_ip())
            connection = Connection.IPVanishConnection(country_id)
            print('connecting...')
            connection.connect()
            print('connected to ' + country_id)
            print('IP while using VPN', Connection.get_ip())

            html_code_of_the_page = requests.get(url).text

            # save html code of the page (input: url, html_code_of_the_page)
            test_data.save_webpage(html_code_of_the_page, url, country_id)

            # close the connection
            connection.close()
            print('closed')
            print('IP after using VPN', Connection.get_ip())
        pass

    # returns list of first n urls from AntiZapret
    def get_list_of_first_n_urls_from_antizapret(self, number_of_urls):
        request_a_List_of_blocked_websites = requests.get('http://api.antizapret.info/all.php?type=json')
        # decode the received data
        list_of_blocked_websites = json.loads(request_a_List_of_blocked_websites.text)['register']
        list_of_urls = []
        for blocked_website in list_of_blocked_websites[:number_of_urls]:
            list_of_urls.append(blocked_website['url'])
        return list_of_urls


# # Examples:
# collectDataHandler = CollectData()
# print(collectDataHandler.getListOfFirstNurlsFromAntiZapret(10))
# collectDataHandler.collectMultipleWebpagesFromASingleCountry(1, 2, 1)