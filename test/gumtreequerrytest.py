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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRaisesOnEmptyCity']
    unittest.main()