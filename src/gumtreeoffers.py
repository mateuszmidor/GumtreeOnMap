# -*- coding: UTF-8 -*-

import Queue
import time

from geocoder import Geocoder
from offerfetcher import OfferFetcher
from addressresolver import AddressResolver
from gumtreeofferurls import GumtreeOfferUrls


    
class GumtreeOffers():
     
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
            
        # fetch offers in separate threads
        for url in GumtreeOfferUrls.getUrls(gumtreeQuerry, count):
            inQueue.put(url)
            
        # wait for all pages to be processed
        inQueue.join()
        
        offers = []
        while (not outQueue.empty()):
            offers.append(outQueue.get())
            
        return offers
                    
    @staticmethod
    def addAddressToEachOffer(offers):
        offersWithAddress = []
        for offer in offers:
            offerWithAddress = dict(offer) # make a copy not to affect original offer
            offerWithAddress['address'] = AddressResolver.resolve(defaulAddress = "Krakow",
                                                                  offer["addressSection"],
                                                                  offer["title"],
                                                                  offer["summary"]) 
            offersWithAddress.append(offerWithAddress)
            
        return offersWithAddress
    
    @staticmethod
    def addGeocoordsToEachOffer(offers):
        offersWithCoords = []
        for offer in offers:
            offerWithCoords = dict(offer) # make a copy not to affect original offer
            offerWithCoords['longlatt'] = Geocoder.getCoordinates(offer["address"])
            offersWithCoords.append(offer)
            
        return offersWithCoords
    
    @staticmethod 
    def askForOffers(gumtreeQuerry, numOffers):
        offers = GumtreeOffers.fetchOffers(gumtreeQuerry, numOffers)
        offers = GumtreeOffers.addAddressToEachOffer(offers)
        offers = GumtreeOffers.addGeocoordsToEachOffer(offers)
        return offers   
   
    
#--------------------------- DEMO
if (__name__ == "__main__"):
    querry = u"http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=120000"

    offers = GumtreeOffers.askForOffers(querry, 37)
    FORMATTER = u"{0} - {1}, {2}\n{3}\n{4}\n{5}\n{6}\n{7}\n"
    for i, offer in enumerate(offers):
        print "*" * 20
        print i + 1
        print FORMATTER.format(offer["title"],
                               offer["date"],
                               offer["price"],
                               offer["address"],
                               offer["lonlat"],
                               offer["summary"],
                               offer["imageUrl"],
                               offer["url"])

