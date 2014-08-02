'''
Created on 30-07-2014

@author: mateusz
'''
from urlfetcher import UrlFetcher
import gumtreeofferparser as Parser
import threading



    
class OfferFetcher(threading.Thread):
    def __init__(self, inQueue, outQueue, documentFetcher = UrlFetcher):
        threading.Thread.__init__(self)
        self.inQueue = inQueue
        self.outQueue = outQueue
        self.documentFetcher = documentFetcher


    def fetchDocument(self, url):
        return self.documentFetcher.fetchDocument(url)

    def getOffer(self, url):
        html = self.fetchDocument(url)
        
        title = Parser.extractTitle(html)
        date = Parser.extractDate(html)
        price = Parser.extractPrice(html)
        addressSection = Parser.extractAddress(html)
        description = Parser.extractDescription(html)
        summary = Parser.extractSummary(html)
        imageUrl = Parser.extractImageUrl(html)
        
        offer = {"title" : title,
                 "date" : date,
                 "price" : price,
                 "addressSection" : addressSection,
                 "description" : description,
                 "summary" : summary,
                 "url" : url,
                 "imageUrl" : imageUrl}
        
        return offer
    
    def run(self):
        while (True):
            url = self.inQueue.get()       
            offer = self.getOffer(url)
            self.outQueue.put(offer)
            self.inQueue.task_done()