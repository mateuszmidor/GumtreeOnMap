# -*- coding: utf-8 -*-
import os
import sys
import time
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

def fetchOffers(querry, numPages = 1):
    offers = []
    for i in range(numPages):
        offers += querryoffersource.getOffers(querry + str(i+1))

    return offers

def saveMapAsHtmlPage(gmap, filename):
    outputHtmlFilename = filename
    with open(outputHtmlFilename,'wb') as f:
        f.write(gmap.showHtml())

    print "Map saved in ", outputHtmlFilename
    
def run():
    gmap = getGoogleMapForKrakow()
    directory = os.path.dirname(os.path.realpath(sys.argv[0]))
    filename = os.path.join(directory, 'OfferMap.html') 
    

    print "Fetching offers"
    querry = gumtreequerrybuilder.build(city='Krakow' )
    offers = fetchOffers(querry, 1)

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







