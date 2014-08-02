'''
Created on 01-08-2014

@author: mateusz
'''
import unittest
from googlemappoints import GoogleMapPoints


class Test(unittest.TestCase):

    def setUp(self):
        offer1 = {"title" : "title1",
                 "date" : "date1",
                 "price" : "price1",
                 "addressSection" : "addressSection1",
                 "description" : "description1",
                 "summary" : "summary1",
                 "url" : "url1",
                 "imageUrl" : "imageUrl1"}
        
        offer2 = {"title" : "title2",
                 "date" : "date2",
                 "price" : "price2",
                 "addressSection" : "addressSection2",
                 "description" : "description2",
                 "summary" : "summary2",
                 "url" : "url2",
                 "imageUrl" : "imageUrl2"}        
        
        self.locations = {'Pawlickiego 2' : {'longlatt' : [50.01, 10.01],
                                            'offers' : [offer1]},
                         'Starowislna 30' :{'longlatt' : [50.09, 10.09],
                                            'offers' : [offer2]}
                          }

    def extractPoints(self, javaScriptPointList):
        """ [[50.11, 10.54, 'Nowe mieszkanie w centrum...', icon_today], [...]] """
        js = javaScriptPointList
        js = js[2:-2] # remove outer [[ and ]]
        items = js.split('], [') # extract items seperated by '], ['
        p1 = items[0].split(", ") # extract fields seperated by ', '
        p2 = items[1].split(", ")
        return p1, p2
        
    def testEmptyMapPointListAsJavaScript(self):
        locations = {}
        mapPoints = GoogleMapPoints.fromLocations(locations)
        js = mapPoints.asJavaScript()
        self.assertEquals("[]", js) #empty point list

    def testMapPointListAsJavaScript(self):
        locations = self.locations
        mapPoints = GoogleMapPoints.fromLocations(locations)
        js = mapPoints.asJavaScript()  
        p1, p2 = self.extractPoints(js)
        
        self.assertEquals('50.01', p1[0])
        self.assertEquals('10.01', p1[1])
        # p1[2] is html description, and can be arbitrarily formed so - skip it
        self.assertEquals('icon_older', p1[3])
        
        self.assertEquals('50.09', p2[0])
        self.assertEquals('10.09', p2[1])
        # p2[2] is html description, and can be arbitrarily formed so - skip it
        self.assertEquals('icon_older', p2[3])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEmptyPointListAsJavaScript']
    unittest.main()