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
    listOfDefinitelyBlockedPages = [{'url': 'http://leonwolf.livejournal.com', 'ip': '208.93.0.190'},
                                    {'url': 'http://navalny.livejournal.com', 'ip': '208.93.0.190'}]

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
        """
        if country_id is not None:
            connection = Connection.IPVanishConnection(country_id)
        else:
            connection = Connection.DirectConnection()
        """
        # TODO: after debugging, comment the following line out and use part above
        connection = Connection.DirectConnection()

        print('connecting...')
        connection.connect()
        print('connected to ' + country_id)
        print('IP while using VPN', Connection.get_ip())

        # listOfBlockedWebsites = []
        if (use_manually_selected_list):
            listOfBlockedWebsites = self.listOfDefinitelyBlockedPages
        else:
            requestAListOfBlockedWebsites = requests.get('http://api.antizapret.info/all.php?type=json')
            # decode the received data
            listOfBlockedWebsites = json.loads(requestAListOfBlockedWebsites.text)['register']
        # go through websites in the list
        for blockedWebsite in listOfBlockedWebsites[:number_of_webpages]:  # first n results
            blockedURL = blockedWebsite['url']
            htmlCodeOfThePage = requests.get(blockedURL, timeout=8).text  # timeout = 8 seconds

            # print(blockedURL)
            # print(htmlCodeOfThePage)

            # save html code of the page (input: blockedURL, htmlCodeOfThePage)
            test_data.save_webpage(htmlCodeOfThePage, blockedURL, country_id)

        # close the connection
        connection.close()
        print('closed')
        print('IP after using VPN', Connection.get_ip())

    # access a single webpage from multiple countries
    # TODO: Update later this method
    def collectOneWebpageFromMultipleCoutries(self, listOfCountryIDs, url, testData):
        for countryID in listOfCountryIDs:
            # open the connection using countryID
            print('IP before using VPN', Connection.get_ip())
            connection = Connection.IPVanishConnection(countryID)
            print('connecting...')
            connection.connect()
            print('connected to ' + countryID)
            print('IP while using VPN', Connection.get_ip())

            htmlCodeOfThePage = requests.get(url).text

            # save html code of the page (input: url, htmlCodeOfThePage)
            testData.save_webpage(htmlCodeOfThePage, url, countryID)

            # close the connection
            connection.close()
            print('closed')
            print('IP after using VPN', Connection.get_ip())
        pass

    # returns list of first n urls from AntiZapret
    def getListOfFirstNurlsFromAntiZapret(self, numberOfURLS):
        requestAListOfBlockedWebsites = requests.get('http://api.antizapret.info/all.php?type=json')
        # decode the received data
        listOfBlockedWebsites = json.loads(requestAListOfBlockedWebsites.text)['register']
        listOfURLs = []
        for blockedWebsite in listOfBlockedWebsites[:numberOfURLS]:
            listOfURLs.append(blockedWebsite['url'])
        return listOfURLs


# # Examples:
# collectDataHandler = CollectData()
# print(collectDataHandler.getListOfFirstNurlsFromAntiZapret(10))
# collectDataHandler.collectMultipleWebpagesFromASingleCountry(1, 2, 1)