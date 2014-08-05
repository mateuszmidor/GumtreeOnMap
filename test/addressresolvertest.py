'''
Created on 02-08-2014

@author: mateusz
'''
import unittest
from addressresolver import AddressResolver

class Test(unittest.TestCase):

    def testResolveStreetWithNumber(self):
        address = u"Wielicka 2, Krakow"
        source = u"Do wynajecia przytulne mieszkanie pod adresem %s \n 3 pokoje w cenie dwoch" % address
        resolved = AddressResolver.resolve(u'krakow', source)
        self.assertEquals(u"wielicka 2, krakow, polska", resolved)
        
    def testResolveDistrict(self):
        address = u"Ruczaj"
        source = u"Do wynajecia przytulne mieszkanie w dzielnicy %s \n 3 pokoje w cenie dwoch" % address
        resolved = AddressResolver.resolve(u'krakow', source)
        self.assertEquals(u"ruczaj, krakow, polska", resolved)

    def testResolveFailAndFallbackToCityOnly(self):
        address = u"Łodygowice" # theres no łodygowice in krakow :)
        source = u"Do wynajecia przytulne mieszkanie w dzielnicy %s \n 3 pokoje w cenie dwoch" % address
        resolved = AddressResolver.resolve(u'krakow', source)
        self.assertEquals(u'krakow, polska', resolved)        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testResolveStreetWithNumber']
    unittest.main()