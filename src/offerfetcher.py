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
        Thread.__init__(self, name="OfferFetcher")
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
        offer = Parser.extractOffer(html)
        offer["url"] = url
        return offer