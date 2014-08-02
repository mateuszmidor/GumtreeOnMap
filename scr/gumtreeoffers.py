# -*- coding: UTF-8 -*-

import Queue
import time

from geocoder import Geocoder
from offerfetcher import OfferFetcher
from gumtreeofferurls import GumtreeOfferUrls


    
class GumtreeOffers():   
    @staticmethod 
    def askForOffers(gumtreeQuerry, numOffers):
        
        inQueue = Queue.Queue()
        outQueue = Queue.Queue()
    
        NUM_THREADS = 8
        # prepare working threads
        for i in xrange(NUM_THREADS):
            t = OfferFetcher(inQueue, outQueue)
            t.setDaemon(True)
            t.start()     
            
        # fetch offers in separate threads
        for url in GumtreeOfferUrls.getUrls(gumtreeQuerry, numOffers):
            inQueue.put(url)
            
    
        # wait for all pages to be processed
        print "Waiting for %s threads to finish processing pages..." % NUM_THREADS
        inQueue.join()
        print "Finished"
        offers = []
    
        while (not outQueue.empty()):
            offer = outQueue.get()
            lonlat =  Geocoder.getCoordinates(offer["address"] + ", Krakow, Polska")
            time.sleep(0.1)
            offer["lonlat"] = lonlat,
            offers.append(offer)
            
            
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

