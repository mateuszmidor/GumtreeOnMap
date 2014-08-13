'''
Created on 12-08-2014

@author: mateusz
'''
import unittest
import setupdependencyinjectiontest  # @UnusedImport setups dependency injection for tests
from injectdependency import InjectDependency
from gumtreeofferswithcache import GumtreeOffersWithCache

# this guy is used by GumtreeOffersWithCache
class OfferUrlsStub():
    @staticmethod
    def getUrls(querryUrl, count):
        return ["url1", "url2", "url3"]
    
# this guy is used by GumtreeOffersWithCache
class OfferFetcherMock():
    offerlist = []
    def __init__(self, cityAddressResolver, numThreads):
        pass
    
    def enqueueUrl(self, url):
        URL_TO_OFFER = {"url1" : "offer1",
                        "url2" : "offer2"}
        offer = URL_TO_OFFER[url]
        self.offerlist.append(offer)
        
    def offers(self):
        return self.offerlist
    
# this guy is used by GumtreeOffersWithCache
class AddressResolverStub():
    @staticmethod
    def forCity(city):
        return None
   
class QuerryStub():
    city = "[value not used]"
    def __str__(self):
        return "[value not used]"
     

    
class GumtreeOffersWithCacheTest(unittest.TestCase):
    def setUp(self):
        offercache = {"url3" : "offer3"}
        InjectDependency.manualInject('offercache', offercache, GumtreeOffersWithCache)
        InjectDependency.manualInject('addressresolver', AddressResolverStub, GumtreeOffersWithCache)
        InjectDependency.manualInject('offerurls', OfferUrlsStub, GumtreeOffersWithCache)
        InjectDependency.manualInject('offerfetcher', OfferFetcherMock, GumtreeOffersWithCache)

    def testAskForOffers(self):
        querry = QuerryStub()
        offers = GumtreeOffersWithCache.askForOffers(querry, 1)
        
        self.assertEquals(3, len(offers))
        self.assertTrue("offer1" in offers) # from fetcher
        self.assertTrue("offer2" in offers) # from fetchre
        self.assertTrue("offer3" in offers) # from cache


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()