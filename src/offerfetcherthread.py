'''
Created on 30-07-2014

@author: mateusz
'''
from threading import Thread
import gumtreeofferparser as Parser
from injectdependency import Inject, InjectDependency

@InjectDependency('urlfetcher', 'geocoder', 'logger') 
class OfferFetcherThread(Thread):
    """
        you create this thread with inQueue and outQueue, 
        and city adddress resolver,
        then you put url to gumtree flat offer on inQueue
        and get fetched, parsed, geocoded offer from outQueue.
        This allowes for parallel offer fetching.
        Simple!
    """
    urlfetcher = Inject
    geocoder = Inject
    logger = Inject
    
    def __init__(self, inQueue, outQueue, addressresolver):
        Thread.__init__(self, name="OfferFetcherThread")
        self.setDaemon(True)
        self.inQueue = inQueue
        self.outQueue = outQueue
        self.addressresolver = addressresolver

    def run(self):
        while (True): # this is ok for daemon thread
            try:
                url = self.inQueue.get()       
                offer = self.getOffer(url)
                self.outQueue.put(offer)
            except Exception, e:
                self.logger.exception(e)
            finally:
                self.inQueue.task_done()

    def getOffer(self, url):
        html = self.urlfetcher.fetchDocument(url)
        offer = Parser.extractOffer(html)
        offer = self.addUrl(url, offer)
        offer = self.addAddress(offer)
        offer = self.addGeocoding(offer)
        return offer
    
    def addUrl(self, url, offer):
        offerWithUrl = dict(offer)
        offerWithUrl["url"] = url
        return offerWithUrl
        
    def addAddress(self, offer):
        offerWithAddress = dict(offer) # make a copy not to affect original offer
            
        # lets try to find more accurate address than only the supplied city name
        offerWithAddress['address'] = self.addressresolver.resolve(offer["addressSection"],
                                                                   offer["title"],
                                                                   offer["summary"]) 
        return offerWithAddress
    
    def addGeocoding(self, offer):
        offerWithCoords = dict(offer) # make a copy not to affect original offer
        offerWithCoords['longlatt'] = self.geocoder.getCoordinates(offer["address"])
        return offerWithCoords