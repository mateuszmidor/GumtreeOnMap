'''
Created on 12-08-2014

@author: mateusz
'''
import unittest
from parallelgumtreeofferfetcher import ParallelGumtreeOfferFetcher
from threading import Thread

class FetcherThreadMock(Thread):
    def __init__(self, inQueue, outQueue, addressresolver):
        Thread.__init__(self)
        self.setDaemon(True)
        self.inQueue = inQueue
        self.outQueue = outQueue
        
    def run(self):
        # just move one item from inQueue to outQueue
        item = self.inQueue.get()
        self.outQueue.put(item)
        self.inQueue.task_done()
                  
class Test(unittest.TestCase):

    def testParallelGetOffers(self):
        fetcher = ParallelGumtreeOfferFetcher(None, 3, FetcherThreadMock)
        fetcher.enqueueUrl("offer1")
        fetcher.enqueueUrl("offer2")
        fetcher.enqueueUrl("offer3")
        
        offers = fetcher.offers()
        self.assertEquals(3, len(offers))
        self.assertTrue("offer1" in offers)
        self.assertTrue("offer2" in offers)
        self.assertTrue("offer3" in offers)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()