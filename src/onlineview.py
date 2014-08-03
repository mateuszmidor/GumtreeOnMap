'''
Created on 03-08-2014

@author: mateusz
'''
from webpagetemplate import WebPageTemplate
from locations import Locations
from googlemappoints import GoogleMapPoints
from geocoder import Geocoder
from httpresponse import HttpResponse

class OnlineView():
    '''
    classdocs
    '''

    @staticmethod
    def render(offers, city):
        locations = Locations.fromOffers(offers)
        mapPoints = GoogleMapPoints.fromLocations(locations)
        mapCenter = Geocoder.getCoordinates(city)
        mapZoom = 12 # this should be evaluated or predefined to ensure best map look 
        offerPage = OnlineView.getOfferPage(mapPoints, mapCenter, mapZoom)
        HttpResponse.renderPage(offerPage.getHtml())
        
    @staticmethod
    def getOfferPage(mapPoints, mapCenter, mapZoom):
        offerPage = WebPageTemplate.fromFile("../data/OnlineView.htm")
        offerPage.setField(u"$POINTS$", mapPoints.asJavaScript())
        offerPage.setField(u"$MAP_CENTER_LONG$", mapCenter[0])
        offerPage.setField(u"$MAP_CENTER_LATT$", mapCenter[1])
        offerPage.setField(u"$MAP_ZOOM$", mapZoom)
        return offerPage
