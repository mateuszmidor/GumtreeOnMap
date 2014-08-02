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
        resolved = AddressResolver.resolve(u'defaultAddress', source)
        self.assertEquals(u"wielicka 2", resolved)
        
    def testResolveDistrict(self):
        address = u"Ruczaj"
        source = u"Do wynajecia przytulne mieszkanie w dzielnicy %s \n 3 pokoje w cenie dwoch" % address
        resolved = AddressResolver.resolve(u'defaultAddress', source)
        self.assertEquals(u"ruczaj", resolved)

    def testResolveFallbackToDefaultAddres(self):
        address = u"Łodygowice"
        source = u"Do wynajecia przytulne mieszkanie w dzielnicy %s \n 3 pokoje w cenie dwoch" % address
        resolved = AddressResolver.resolve(u'defaultAddress', source)
        self.assertEquals(u"defaultAddress", resolved)        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testResolveStreetWithNumber']
    unittest.main()