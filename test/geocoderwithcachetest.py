'''
Created on 03-08-2014
 
@author: mateusz
'''
import unittest
from geocoderwithcache import GeocoderWithCache
    
# This guy is used by GeocoderWithCache for geocoding addresses that are not in cache     
class GeocoderStub():
    @staticmethod
    def getCoordinates(address):
        if (address == u"dauna, kraków, polska"):
            return [10, 20]
        else:
            raise Exception("Unknown address provided to GeocoderStub: " + address)
 
 
class Test(unittest.TestCase):
    def setUp(self):
        geocoder = GeocoderWithCache(GeocoderStub) 
        geocoder.registerAddress(u"WIELICKA 2, KRAKÓW, POLSKA", [50.01, 10.09]) # should be case insensitive
        geocoder.registerAddress(u"starowiślna 30, kraków, polska", [50.03, 10.04])
        self.geocoderUnderTest = geocoder
       
    def testGetCoordsFromCachedAddress1(self):
        EXPECTED_COORDS = [50.01, 10.09] # from knownAddresses
        coords = self.geocoderUnderTest.getCoordinates(u"wielicka 2, kraków, polska")
        self.assertEquals(EXPECTED_COORDS, coords)
           
    def testGetCoordsFromCachedAddress2(self):
        EXPECTED_COORDS = [50.03, 10.04] # from knownAddresses
        coords = self.geocoderUnderTest.getCoordinates(u"starowiślna 30, kraków, polska")
        self.assertEquals(EXPECTED_COORDS, coords)
       
    def testGetCoordsFromNewAddress(self):
        EXPECTED_COORDS = [10, 20]  # from GeocoderStub
        coords = self.geocoderUnderTest.getCoordinates(u"dauna, kraków, polska") 
        self.assertEquals(EXPECTED_COORDS, coords)
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetCoordsFromKnownAddress']
    unittest.main()