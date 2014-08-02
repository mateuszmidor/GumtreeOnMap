'''
Created on 02-08-2014

@author: mateusz
'''
import unittest
from gumtreequerry import GumtreeQuerry


class Test(unittest.TestCase):

    def testRaisesOnEmptyCity(self):
        try:
            GumtreeQuerry.compose(city="")
            self.fail("Empty city param should cause exception")
        except ValueError:
            # valid case
            pass
        except:
            self.fail("Unexpected exception type thrown")

    def testAllParamsSupplied(self):
        EXPECTED_QUERRY_STRING = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/Krakow/Nowa+Huta/c9008l3200208?A_AreaInMeters_max=70&A_AreaInMeters_min=30&A_ForRentBy=ownr&A_NumberRooms=10&AdType=2&isSearchForm=true&maxPrice=1000&maxPriceBackend=200000&minPrice=500&minPriceBackend=100000'
        querry = GumtreeQuerry.compose(city="Krakow", 
                                       whereabouts="Nowa Huta", 
                                       numRooms="1", 
                                       minPrice="500", 
                                       maxPrice="1000",
                                       minArea="30",
                                       maxArea="70")
        self.assertEquals(EXPECTED_QUERRY_STRING, str(querry))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRaisesOnEmptyCity']
    unittest.main()