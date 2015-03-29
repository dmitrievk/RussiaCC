__author__ = 'JesseBrizzi'
# sample usage
# ----------------------------------------------------------------
# test = WebData()
#
# test.save_webpage('test', 'www.test.com', 'test1-ip.vanish.com')
# test.save_webpage('test', 'www.test.com', 'test2-ip.vanish.com')
#
# temp = test.get_webpage('www.test.com', 'test1-ip.vanish.com')
#
# print(temp) # prints the html array
#
# tempArray = test.get_all_webpages('www.test.com')
#
# print(tempArray) # prints the dictionary of html arrays

import datetime
from os.path import expanduser
import os


def valid_file_name(name):
    # handle these characters / ? < > \ : * | "
    name = name.replace('/', '-')
    name = name.replace('?', '-')
    name = name.replace('<', '-')
    name = name.replace('>', '-')
    name = name.replace('\\', '-')
    name = name.replace(':', '-')
    name = name.replace('*', '-')
    name = name.replace('|', '-')
    name = name.replace('"', '-')
    return name


class WebData:
    homeDir = ''
    nameDir = ''
    def __init__(self, name=None):
        # this is so you can call the class and access a previous run of the data collection
        if name is None:
            # get the current datetime to name the directory
            name = datetime.datetime.now().replace(microsecond=0).isoformat('_')
            name = valid_file_name(name)

        # get the home dir (user dir in windows, home in unix)
        self.homeDir = expanduser("~")

        # combine the strings in a way that is cross platform
        self.nameDir = os.path.join(self.homeDir, name)

        # check to see if the directory already exists
        if not os.path.exists(self.nameDir):
            os.makedirs(self.nameDir)

    # takes in 3 strings, one for the VPN that was used for this data, the web address, and the actual HTML
    # if no vpn is given it assumes that it was collected using the local conection and names the flder local.
    def save_webpage(self, html, address, vpn=None):
        if vpn is None:
            vpn = 'local'

        # checks to see if this is the first page to save to a folder and creates the dir if it needs to.
        saveDir = os.path.join(self.nameDir, vpn)

        if not os.path.exists(saveDir):
            os.makedirs(saveDir)

        # saves the webpage in the dir, will overwrite old save.
        fullFile = os.path.join(saveDir, valid_file_name(address) + '.html')

        html_file = open(fullFile, "w")
        html_file.write(html)
        html_file.close()

    # returns a string array of a specific webpage from a specific vpn
    def get_webpage(self, address, vpn):
        saveDir = os.path.join(self.nameDir, vpn)
        fullFile = os.path.join(saveDir, valid_file_name(address) + '.html')

        if os.path.isfile(fullFile):
            with open(fullFile, "r") as f:
                content = f.readlines()
            return content

        return []

    # gets a dictionary of all of the examples of a single webpage, the dictionary key are the vpn names
    def get_all_webpages(self, address):
        out = {}

        for root, dirs, files in os.walk(self.nameDir, topdown=False):
            for d in dirs:
                temp = self.get_webpage(address, d)
                if temp:
                    out[d] = temp

        return out