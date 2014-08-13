'''
Created on 11-08-2014

@author: mateusz
'''
import Queue
from offerfetcherthread import OfferFetcherThread

class ParallelGumtreeOfferFetcher():
    
    @classmethod
    def parallelWithAddressResolutionAndGeocoding(cls, cityAddressResolver, numThreads):
        return cls(cityAddressResolver, numThreads)
    
    def __init__(self, cityAddressResolver, numThreads = 2, FetcherThread = OfferFetcherThread):
        self.inQueue = Queue.Queue()    
        self.outQueue = Queue.Queue()
        
        # prepare working threads
        for i in xrange(numThreads):  # @UnusedVariable
            t = FetcherThread(self.inQueue, self.outQueue, cityAddressResolver)
            t.start() 
            
    def enqueueUrl(self, url):
        self.inQueue.put(url)
        
    def offers(self):
        # wait for all threads to be process pages
        self.inQueue.join()        
      
        offers = []
        while (not self.outQueue.empty()):
            offers.append(self.outQueue.get())
            
        return offers   