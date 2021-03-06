'''
Created on 03-08-2014

@author: mateusz
'''
from webpagetemplate import WebPageTemplate
from locations import Locations
from googlemappoints import GoogleMapPoints
from httpresponse import HttpResponse
from injectdependency import InjectDependency, Inject

@InjectDependency('geocoder', 'logger')
class OnlineView():
    geocoder = Inject
    logger = Inject
    
    @staticmethod
    def render(offers, query):
        locations = Locations.fromOffers(offers)
        mapPoints = GoogleMapPoints.fromLocations(locations)
        mapCenter = OnlineView.getMapCenter(query.city)
        mapZoom = 12 # this should be evaluated  to ensure best map look 
        
        offerPage = OnlineView.getOfferPage(mapPoints, mapCenter, mapZoom, 
                                            query.numRooms,
                                            query.maxPrice,
                                            query.whereabouts)
        HttpResponse.renderPage(offerPage.getHtml())

    @staticmethod
    def getMapCenter(city):
        try:
            return OnlineView.geocoder.getCoordinates(city)
        except Exception, e:
            OnlineView.logger.exception(e)
            return (50.0646501, 19.9449799) #krakow
        
    @staticmethod
    def getOfferPage(mapPoints, mapCenter, mapZoom, numRooms, maxPrice, whereabouts):
        offerPage = WebPageTemplate.fromFile("data/OnlineView.htm")
        offerPage.setField(u"$POINTS$", mapPoints.asJavaScript())
        offerPage.setField(u"$MAP_CENTER_LONG$", mapCenter[0])
        offerPage.setField(u"$MAP_CENTER_LATT$", mapCenter[1])
        offerPage.setField(u"$MAP_ZOOM$", mapZoom)
        offerPage.setField(u"$NUM_ROOMS$", numRooms)
        offerPage.setField(u"$MAX_PRICE$", maxPrice)
        offerPage.setField(u"$WHEREABOUTS$", whereabouts)
        
        return offerPage

