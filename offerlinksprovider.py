'''
Created on 23-07-2014

@author: mateusz
'''

# -*- coding: UTF-8 -*-

import re
from urlfetcher import UrlFetcher

class OfferLinksProvider:
    def __init__(self, querry, limit):
        self.querry = querry # gumtree querry for offer
        self.limit = limit # max number of urls to return
        self.currUrlNumber = 0 # current url no
        self.urls = [] # url list to return
        self.currPage = 1 # current offers page no, we start from page 1
        self.hasNextPage = True # is there a next page to fetch offers from?
        
    def __iter__(self):
        return self
    
    def next(self):
        url = self.nextUrl()
        return url
        
        
    def nextUrl(self):
        # limit hit - stop iteration
        if (self.currUrlNumber == self.limit):
            raise StopIteration()
        
        # fetch urls if list empty
        if (not self.urls):
            self.urls = self.fetchUrls()

        # increase returned url counter
        self.currUrlNumber += 1

        # and return url
        return self.urls.pop()
        
    def fetchUrls(self):
        # if no more pages to fetch urls from - stop iteration
        if (not self.hasNextPage):
            raise StopIteration()

        # add page number to offers querry
        offersPageUrl = "{0}&Page={1}".format(self.querry, self.currPage)
        html = UrlFetcher.fetch(offersPageUrl)
        self.hasNextPage = self.getHasNextPage(html)
        self.currPage += 1
        
        return self.extractOfferUrls(html)
        
    def getHasNextPage(self, html):
        NEXT_PAGE_TAG = u'class="prevNextLink">Następne'
        
        if (NEXT_PAGE_TAG in html):
            return True
        else:
            return False       
        
    def extractUrlFromHtml(self, html):
        pattern = 'a href="([^"]*)'
        return re.search(pattern, html).group(1)
    
    def extractOfferUrls(self, html):
        START_TAG = '<div class="ar-title">'
        STOP_TAG = '</div>'
        urls = set([])
        
        iStart = html.find(START_TAG)
        while (iStart != -1):
            iStop = html.find(STOP_TAG, iStart)
    
            # a href=http://...
            htmlLink = html[iStart + len(START_TAG):iStop]
    
            # http://...
            url = self.extractUrlFromHtml(htmlLink)
            urls.add(url)
            iStart = html.find(START_TAG, iStop)
    
        return urls
    
    
#--------------------------- DEMO
if (__name__ == "__main__"):
    querry = "http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=120000"
    for i, url in enumerate(OfferLinksProvider(querry, 27)):
        print i + 1
        print url
        
