'''
Created on 30-07-2014

@author: mateusz
'''
import unittest
from locations import Locations


class LocationsTest(unittest.TestCase):

    def testLocations(self):
        offer1 = {'address' : 'Wielicka 9',
                  'longlatt' : [51, 11],
                  'title' : 'Mieszkanie dwupokojowe'}
        offer2 = {'address' : 'Wielicka 9',
                  'longlatt' : [51, 11],
                  'title' : 'Mieszkanie trzypokojowe'}
        offer3 = {'address' : 'Sarego 12',
                  'longlatt' : [53, 13],
                  'title' : 'Garsoniera wysoki standard'}
        
        offers = [offer1, offer2, offer3]
        locations = Locations.fromOffers(offers)
        
        self.assertTrue(locations.has_key('Wielicka 9'), "Locations does not contain required address")
        self.assertEquals(2, len(locations['Wielicka 9']['offers']), "Should be 2 offers at this location")
        self.assertEquals([51, 11], locations['Wielicka 9']['longlatt'])
        self.assertEquals('Mieszkanie dwupokojowe', locations['Wielicka 9']['offers'][0]['title'])
        self.assertEquals('Mieszkanie trzypokojowe', locations['Wielicka 9']['offers'][1]['title'])
        
        self.assertTrue(locations.has_key('Sarego 12'), "Locations does not contain required address")
        self.assertEquals(1, len(locations['Sarego 12']['offers']), "Should be 1 offer at this location")
        self.assertEquals([53, 13], locations['Sarego 12']['longlatt'])
        self.assertEquals('Garsoniera wysoki standard', locations['Sarego 12']['offers'][0]['title'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()