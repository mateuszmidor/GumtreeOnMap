'''
Created on 31-07-2014

@author: mateusz
'''
from locations import Locations
from googlemappoints import GoogleMapPoints
from webpagetemplate import WebPageTemplate

class DesktopView():
    
    @staticmethod
    def render(offers):
        locations = Locations.fromOffers(offers)
        mapPoints = GoogleMapPoints.fromLocations(locations)
        offerPage = WebPageTemplate.fromFile("../data/DesktopView.html")
        offerPage.setField(u"$POINTS$", mapPoints.asJavaScript())
        offerPage.saveToFile("OfferMap.html")
        
        
        