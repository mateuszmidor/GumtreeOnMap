# -*- coding: UTF-8 -*-

import re
from injectdependency import InjectDependency, Inject

@InjectDependency('urlfetcher')
class GumtreeOfferUrls():
    urlfetcher = Inject
    
    @staticmethod
    def getUrls(querry, limit):
        urls = GumtreeOfferUrls(querry, limit)
        
        # url generator
        while(True):
            try:
                yield urls.nextUrl()
            except StopIteration:
                return

    def __init__(self, querry, limit):
        self.querry = querry # gumtree querry for offer
        self.limit = limit # max number of urls to return
        self.currUrlNumber = 0 # current url no
        self.urls = [] # url list to return
        self.currPage = 1 # current offers page no, we start from page 1
        self.hasNextPage = True # is there a next page to fetch offers from?

    def nextUrl(self):
        # limit hit - stop iteration
        if (self.currUrlNumber == self.limit):
            raise StopIteration()
        
        # fetch urls if list empty
        if (not self.urls):
            self.urls = self.fetchUrls()

        # check if fetched any urls
        if (not self.urls):
            raise StopIteration()
        
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
        
        # fetch html with offers listed
        html = self.urlfetcher.fetchDocument(offersPageUrl)
        self.hasNextPage = self.getHasNextPage(html)
        self.currPage += 1
        
        return self.extractOfferUrls(html)
        
    def getHasNextPage(self, html):
        NEXT_PAGE_TAG = u'class="prevNextLink">Następne'
        return (NEXT_PAGE_TAG in html)
        
    def extractUrlFromHtmlHiperlink(self, html):
        pattern = u'a href="([^"]*)'
        return re.search(pattern, html).group(1)
    
    def extractOfferUrls(self, html):
        START_TAG = '<div class="ar-title">'
        STOP_TAG = '</div>'
        urls = []
        
        iStart = html.find(START_TAG)
        while (iStart != -1):
            iStop = html.find(STOP_TAG, iStart)
    
            # a href=http://...
            htmlLink = html[iStart + len(START_TAG):iStop]
    
            # http://...
            url = self.extractUrlFromHtmlHiperlink(htmlLink)
            urls.append(url)
            iStart = html.find(START_TAG, iStop)
    
        return urls