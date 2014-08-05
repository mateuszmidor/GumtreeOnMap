'''
Created on 31-07-2014

@author: mateusz
'''
from locations import Locations
from googlemappoints import GoogleMapPoints
from webpagetemplate import WebPageTemplate
from injectdependency import InjectDependency, Inject

@InjectDependency('geocoder')
class DesktopView():
    geocoder = Inject
    
    @staticmethod
    def render(offers, city):
        locations = Locations.fromOffers(offers)
        mapPoints = GoogleMapPoints.fromLocations(locations)
        mapCenter = DesktopView.getMapCenter(city)
        mapZoom = 12 # this should be evaluated to ensure best map look 
        offerPage = DesktopView.getOfferPage(mapPoints, mapCenter, mapZoom)
        offerPage.saveToFile("OfferMap.html")
        
    @staticmethod
    def getMapCenter(city):
        return DesktopView.geocoder.getCoordinates(city)
        
    @staticmethod
    def getOfferPage(mapPoints, mapCenter, mapZoom):
        offerPage = WebPageTemplate.fromFile("../data/DesktopView.htm")
        offerPage.setField(u"$POINTS$", mapPoints.asJavaScript())
        offerPage.setField(u"$MAP_CENTER_LONG$", mapCenter[0])
        offerPage.setField(u"$MAP_CENTER_LATT$", mapCenter[1])
        offerPage.setField(u"$MAP_ZOOM$", mapZoom)
        return offerPage