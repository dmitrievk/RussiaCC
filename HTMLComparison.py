__author__ = 'konstantindmitriev'

from difflib import SequenceMatcher
from WebData import WebData

class HTMLComparison:

    def __init__(self):
        pass

    # compares gathered files between countries and blockingCountry
    # from either current session (session = False) or a particular session (e.g. session = "2015-03-29_12-47-36")
    # returns dictionary: key - country, value - [{url1: difference1 in %}, {url2: difference2 in %} ...]
    def compareFilesBetweenCountries(self, blockingCountry, countries, testData, listOfURLS, session):  #blockingCountry = Russia
        dictOfPercentageOfSimilarity = {}  # key - country, value - [{url1: difference1 in %}, {url2: difference2 in %} ...]
        countries.remove(blockingCountry)
        for country in countries:
            dictOfPercentageOfSimilarity[country] = []


        if session:
                testData.setSession(session)

        for url in listOfURLS:
            dictOfWebpagesFromDifferentVPNServers = testData.get_all_webpages(url)  # keys are the vpn names
            pageFromBlockingCountry = dictOfWebpagesFromDifferentVPNServers[blockingCountry]
            del dictOfWebpagesFromDifferentVPNServers[blockingCountry]

            for country in dictOfWebpagesFromDifferentVPNServers.keys():
                pageFromCurrentCountry = dictOfWebpagesFromDifferentVPNServers[country]
                percentageOfDifference = self.compareTwoHTMLFiles(pageFromBlockingCountry, pageFromCurrentCountry)
                tempList = dictOfPercentageOfSimilarity[country]
                tempList.append({url: percentageOfDifference})
                dictOfPercentageOfSimilarity[country] = tempList #dictOfPercentageOfSimilarity.update({url: percentageOfDifference})

        return dictOfPercentageOfSimilarity

    # compares two html files and returns percent of similarity
    def compareTwoHTMLFiles(self, html1, html2):
        similarity = SequenceMatcher(None, html1, html2)

        return similarity.ratio()*100