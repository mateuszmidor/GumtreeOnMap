# -*- coding: UTF-8 -*-

import Queue
from geocoder import Geocoder
from offerfetcher import OfferFetcher
from addressresolver import AddressResolver
from urlfetcher import UrlFetcher
from gumtreeofferurls import GumtreeOfferUrls

class GumtreeOffers():
     
    @staticmethod
    def fetchOffers(gumtreeQuerry, count, documentFetcher):
        inQueue = Queue.Queue()
        outQueue = Queue.Queue()
    
        # limit by netmark.pl to maximum of 9 threads/python process
        NUM_THREADS = 8
        
        # prepare working threads
        for i in xrange(NUM_THREADS):  # @UnusedVariable
            t = OfferFetcher(inQueue, outQueue, documentFetcher)
            t.setDaemon(True)
            t.start()     
            
        # fetch offers in separate threads as new urls appear in inQueue
        for url in GumtreeOfferUrls.getUrls(gumtreeQuerry, count, documentFetcher):
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
        for offer in offers:
            offerWithAddress = dict(offer) # make a copy not to affect original offer
            
            # lets try to find more accurate address than only the supplied city name
            offerWithAddress['address'] = AddressResolver.resolve(city,
                                                                  offer["addressSection"],
                                                                  offer["title"],
                                                                  offer["summary"]) 
            offersWithAddress.append(offerWithAddress)
            
        return offersWithAddress
    
    @staticmethod
    def addGeocoordsToEachOffer(offers, geocoder):
        offersWithCoords = []
        for offer in offers:
            offerWithCoords = dict(offer) # make a copy not to affect original offer
            offerWithCoords['longlatt'] = geocoder.getCoordinates(offer["address"])
            offersWithCoords.append(offerWithCoords)
            
        return offersWithCoords
    
    @staticmethod 
    def askForOffers(gumtreeQuerry, count, geocoder = Geocoder, documentFetcher = UrlFetcher):
        offers = GumtreeOffers.fetchOffers(str(gumtreeQuerry), count, documentFetcher)
        offers = GumtreeOffers.addAddressToEachOffer(offers, gumtreeQuerry.city)
        offers = GumtreeOffers.addGeocoordsToEachOffer(offers, geocoder)
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

