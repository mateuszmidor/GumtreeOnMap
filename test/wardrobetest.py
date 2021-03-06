﻿'''
Created on 07-08-2014

@author: mateusz
'''
import unittest
from wardrobe import Wardrobe

class Test(unittest.TestCase):

    def testGetItem(self):
        items = {u"łąka" : u"meadow",
                 u"ściemniacz" : u"dimmer"}
        w = Wardrobe.fromDictionary(items)
        
        self.assertEquals(u"meadow", w[u"łąka"])
        self.assertEquals(u"dimmer", w[u"ściemniacz"])
    
    def testSetItem(self):
        w = Wardrobe.fromDictionary({})
        w[u"Środa"] = "Wednesday"
        w[u"Piątek"] = "Friday"    
            
        self.assertEquals("Wednesday", w[u"Środa"])
        self.assertEquals("Friday", w[u"Piątek"])

    def testInOperator(self):
        w = Wardrobe.fromDictionary({})
        w[u"Środa"] = "Wednesday"
        w[u"Piątek"] = "Friday"  
        
        self.assertTrue(u"Środa" in w)
        self.assertTrue(u"Piątek" in w)
        
    def testSupportAsciiKeys(self):
        w = Wardrobe.fromDictionary({})
        w["Środa"] = "Wednesday"
            
        self.assertEquals("Wednesday", w["Środa"])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
