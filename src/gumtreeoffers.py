# -*- coding: UTF-8 -*-

import Queue

import setupdependencyinjection  # @UnusedImport setups dependency injection

from offerfetcher import OfferFetcher
from gumtreeofferurls import GumtreeOfferUrls
from injectdependency import InjectDependency, Inject
import time

@InjectDependency('logger', 'geocoder', 'addressresolver')
class GumtreeOffers():
    logger = Inject
    geocoder = Inject 
    addressresolver = Inject
    
    @staticmethod
    def fetchOffers(gumtreeQuerry, count):
        inQueue = Queue.Queue()
        outQueue = Queue.Queue()
    
        # limit by netmark.pl to maximum of 9 threads/python process
        NUM_THREADS = 8
        
        # prepare working threads
        for i in xrange(NUM_THREADS):  # @UnusedVariable
            t = OfferFetcher(inQueue, outQueue)
            t.setDaemon(True)
            t.start()     
            
        # fetch offers in separate threads as new urls appear in inQueue
        for url in GumtreeOfferUrls.getUrls(gumtreeQuerry, count):
            inQueue.put(url)
            
        # wait for all threads to be process pages
        inQueue.join()
        
        offers = []
        while (not outQueue.empty()):
            offers.append(outQueue.get())
            
        return offers
                    
    @staticmethod
    def addAddressToEachOffer(offers, city):
        offersWithAddress = []
        resolver = GumtreeOffers.addressresolver.forCity(city)
        for offer in offers:
            offerWithAddress = dict(offer) # make a copy not to affect original offer
            
            # lets try to find more accurate address than only the supplied city name
            offerWithAddress['address'] = resolver.resolve(offer["addressSection"],
                                                           offer["title"],
                                                           offer["summary"]) 
            offersWithAddress.append(offerWithAddress)
            
        return offersWithAddress
    
    @staticmethod
    def addGeocoordsToEachOffer(offers):
        offersWithCoords = []
        for offer in offers:
            try: # cant be geocoded then skip this offer
                offerWithCoords = dict(offer) # make a copy not to affect original offer
                offerWithCoords['longlatt'] = GumtreeOffers.geocoder.getCoordinates(offer["address"])
                offersWithCoords.append(offerWithCoords)
            except Exception, e:
                GumtreeOffers.logger.exception(e)
            finally:
                time.sleep(0.1) # google geocoding limit 10/sec max
            
        return offersWithCoords
    
    @staticmethod 
    def askForOffers(gumtreeQuerry, count):
        offers = GumtreeOffers.fetchOffers(str(gumtreeQuerry), count)
        offers = GumtreeOffers.addAddressToEachOffer(offers, gumtreeQuerry.city)
        offers = GumtreeOffers.addGeocoordsToEachOffer(offers)
        return offers   