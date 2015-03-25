__author__ = 'tian'

def get_ip():
    import urllib.request
    return urllib.request.urlopen('http://ip.42.pl/raw').read().decode('ascii')