# -*- coding: utf-8 -*-
import querryoffersource
from geocoder import Geocoder
from googlemap import GoogleMap
from offersasgooglepoints import OffersAsGooglePointsComposer

GUMTREE_QUERRY = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&isSearchForm=true&maxPrice=1600&maxPriceBackend=160000&Page='
DEBNIKI_QUERRY = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/d%C4%99bniki/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&isSearchForm=true&maxPrice=1600&maxPriceBackend=160000&Page='
SRODMIESCIE_QUERRY = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/%C5%9Br%C3%B3dmie%C5%9Bcie/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&isSearchForm=true&maxPrice=1600&maxPriceBackend=160000&Page='

def getGoogleMapForKrakow():
    KRAKOW_PRETTY_ZOOM = 11
    
    gmap = GoogleMap(1200,650)
    gmap.setCenter(Geocoder.getCoordinates("Krakow, Polska"))
    gmap.setZoom(KRAKOW_PRETTY_ZOOM)
    return gmap

def fetchOffers(numPages = 1):
    offers = []
    for i in range(numPages):
        offers += querryoffersource.getOffers(GUMTREE_QUERRY + str(i+1))

    return offers
    
def run():    
    gmap = getGoogleMapForKrakow()
    
    offers = fetchOffers(3)
    points = OffersAsGooglePointsComposer.compose(offers)
    for point in points:
        gmap.addPoint(point)
        
    open('OfferMap.htm','wb').write(gmap.showHtml()) 
    
run()






