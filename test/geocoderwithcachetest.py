'''
Created on 03-08-2014

@author: mateusz
'''
import unittest
from geocoderwithcache import GeocoderWithCache

        
class FakeGeocoder():
    @staticmethod
    def getCoordinates(address):
        if (address == u"dauna, krakow, poland"):
            return [10, 20]
        else:
            raise Exception("Unknown address provided to FakeGeocoder: " + address)


class Test(unittest.TestCase):
    def setUp(self):
        knownAddresses = {u"wielicka 2, krakow, poland" : [50.01, 10.09],
                          u"starowiślna 30, krakow, poland" : [50.03, 10.04]}
        self.geocoderUnderTest = GeocoderWithCache(knownAddresses, FakeGeocoder) 
      
    def testGetCoordsFromKnownAddress1(self):
        EXPECTED_COORDS = [50.01, 10.09] # from knownAddresses
        coords = self.geocoderUnderTest.getCoordinates(u"wielicka 2, krakow, poland")
        self.assertEquals(EXPECTED_COORDS, coords)
          
    def testGetCoordsFromKnownAddress2(self):
        EXPECTED_COORDS = [50.03, 10.04] # from knownAddresses
        coords = self.geocoderUnderTest.getCoordinates(u"starowiślna 30, krakow, poland")
        self.assertEquals(EXPECTED_COORDS, coords)
      
    def testGetCoordsFromNewAddress(self):
        EXPECTED_COORDS = [10, 20]  # from FakeGeocoder
        coords = self.geocoderUnderTest.getCoordinates(u"dauna, krakow, poland") 
        self.assertEquals(EXPECTED_COORDS, coords)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetCoordsFromKnownAddress']
    unittest.main()