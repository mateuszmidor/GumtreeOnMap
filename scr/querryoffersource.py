# -*- coding: UTF-8 -*-

import threading
import Queue
import time

import gumtreeofferparser as parser
from addressextractor import AddressExtractor
from geocoder import Geocoder
from urlfetcher import UrlFetcher
from offerlinksprovider import OfferLinksProvider

streetExtractor = AddressExtractor("data/streets.txt")
districtExtractor = AddressExtractor("data/districts.txt")

    
class OfferFetcher(threading.Thread):
    def __init__(self, inQueue, outQueue):
        threading.Thread.__init__(self)
        self.inQueue = inQueue
        self.outQueue = outQueue

    def getOffer(self, url):
        html = UrlFetcher.fetch(url)
        title = parser.extractTitle(html)
        date = parser.extractDate(html)
        price = parser.extractPrice(html)
        addressSection = parser.extractAddress(html)
        description = parser.extractDescription(html)
        summary = parser.extractSummary(html)
        imageUrl = parser.extractImageUrl(html)
        
        # this is the first place to speedup; longers from 4 -> 10 sec/25offer
        address = streetExtractor.extract(addressSection, title, summary)

        if (not address):
            address = districtExtractor.extract(addressSection, title, summary)
            
        #not found
        if (not address):
            address = "Krakow"
                
        offer = {"title" : title,
                 "date" : date,
                 "price" : price,
                 "addressSection" : addressSection,
                 "address" : address,
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
     
def getOffers(gumtreeQuerry, numOffers):
    
    inQueue = Queue.Queue()
    outQueue = Queue.Queue()

    NUM_THREADS = 8
    # prepare working threads
    for i in xrange(NUM_THREADS):
        t = OfferFetcher(inQueue, outQueue)
        t.setDaemon(True)
        t.start()     
        
    # fetch offers in separate threads
    for url in OfferLinksProvider(gumtreeQuerry, numOffers):
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

    offers = getOffers(querry, 37)
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

