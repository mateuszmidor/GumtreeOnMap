'''
Created on 30-07-2014

@author: mateusz
'''
from threading import Thread
import gumtreeofferparser as Parser
from injectdependency import Inject, InjectDependency

@InjectDependency('urlfetcher') 
class OfferFetcher(Thread):
    urlfetcher = Inject
    
    def __init__(self, inQueue, outQueue):
        Thread.__init__(self)
        self.inQueue = inQueue
        self.outQueue = outQueue

    def run(self):
        while (True): # this is ok for daemon thread
            url = self.inQueue.get()       
            offer = self.getOffer(url)
            self.outQueue.put(offer)
            self.inQueue.task_done()
    
    def getOffer(self, url):
        html = self.urlfetcher.fetchDocument(url)
        
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