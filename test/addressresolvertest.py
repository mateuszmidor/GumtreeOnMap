'''
Created on 02-08-2014
 
@author: mateusz
'''
import unittest
from addressresolver import AddressResolver
 
class AddressExtractorMock():
    
    def __init__(self, result):
        self.result = result
        
    def extract(self, *descriptions):
        return self.result
    
class Test(unittest.TestCase):
      
    def testResolveStreet(self):
        resolver = AddressResolver(u"Krakow", AddressExtractorMock(u"Wielicka"), AddressExtractorMock(None))
        resolved = resolver.resolve("")
        self.assertEquals(u"Wielicka, Krakow, Polska", resolved)
          
    def testResolveDistrict(self):
        resolver = AddressResolver(u"Krakow", AddressExtractorMock(None), AddressExtractorMock(u"Ruczaj"))
        resolved = resolver.resolve("")
        self.assertEquals(u"Ruczaj, Krakow, Polska", resolved)
  
    def testResolveFailAndFallbackToCityOnly(self):
        resolver = AddressResolver(u"Krakow", AddressExtractorMock(None), AddressExtractorMock(None))
        resolved = resolver.resolve("")
        self.assertEquals(u'Krakow, Polska', resolved)  
                 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testResolveStreetWithNumber']
    unittest.main()