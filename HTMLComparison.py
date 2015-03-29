__author__ = 'konstantindmitriev'

import difflib


class HTMLComparison:

    def __init__(self):
        pass

    def compareFilesBetweenTwoCountries(self, country1, country2, testData):



    def compareTwoHTMLFiles(self, html1, html2):
        differ = difflib.HtmlDiff()
        difference = differ.compare(html1, html2)
        print(difference)