'''
Created on 23-07-2014

@author: mateusz
'''

import urllib3 # for thread safety, urllib2 hangs the app

class UrlFetcher:
    @staticmethod
    def fetch(url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        return unicode(r.data, "UTF-8")