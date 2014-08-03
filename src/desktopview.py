'''
Created on 31-07-2014

@author: mateusz
'''
from locations import Locations
from googlemappoints import GoogleMapPoints
from webpagetemplate import WebPageTemplate
from geocoder import Geocoder

class DesktopView():
    
    @staticmethod
    def getOfferPage(mapPoints, mapCenter, mapZoom):
        offerPage = WebPageTemplate.fromFile("../data/DesktopView.htm")
        offerPage.setField(u"$POINTS$", mapPoints.asJavaScript())
        offerPage.setField(u"$MAP_CENTER_LONG$", mapCenter[0])
        offerPage.setField(u"$MAP_CENTER_LATT$", mapCenter[1])
        offerPage.setField(u"$MAP_ZOOM$", mapZoom)
        return offerPage

    @staticmethod
    def render(offers, city):
        locations = Locations.fromOffers(offers)
        mapPoints = GoogleMapPoints.fromLocations(locations)
        mapCenter = Geocoder.getCoordinates(city)
        mapZoom = 12 # this should be evaluated or predefined to ensure best map look 
        offerPage = DesktopView.getOfferPage(mapPoints, mapCenter, mapZoom)
        offerPage.saveToFile("OfferMap.html")
        
        
        