# -*- coding: utf-8 -*-
import os
import sys
import timeit

from offersasgooglepoints import OffersAsGooglePointsComposer
from geocoder import Geocoder
from googlemap import GoogleMap
import querryoffersource
import gumtreequerrybuilder



def getGoogleMapForKrakow():
    KRAKOW_PRETTY_ZOOM = 12    
    gmap = GoogleMap(1200,650)
    gmap.setCenter(Geocoder.getCoordinates("Krakow, Polska"))
    gmap.setZoom(KRAKOW_PRETTY_ZOOM)
    return gmap

def saveMapAsHtmlPage(gmap, filename):
    outputHtmlFilename = filename
    with open(outputHtmlFilename,'wb') as f:
        f.write(gmap.showHtml())

    print "Map saved in ", outputHtmlFilename
    
def run():
    gmap = getGoogleMapForKrakow()
    directory = os.path.dirname(os.path.realpath(sys.argv[0]))
    filename = os.path.join(directory, 'OfferMap.html') 
    
    querry = gumtreequerrybuilder.build(city='Krakow' )

    print "Fetching offers"
    offers = querryoffersource.getOffers(querry, 27)

    print "Composing offers to points on map"
    points = OffersAsGooglePointsComposer.compose(offers)

    print "Adding points to map"
    gmap.addPoints(points)

    print "Saving map as html page"
    saveMapAsHtmlPage(gmap, filename)

    print "Done."
    

total_time = timeit.timeit(run, setup="gc.enable()", number=1)
print "Time taken: ", total_time
#raw_input("Press Enter to exit")







