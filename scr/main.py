#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys
import codecs
import cgi
import timeit
import threading

from offersasgooglepoints import OffersAsGooglePointsComposer
from geocoder import Geocoder
from googlemap import GoogleMap
import querryoffersource
import gumtreequerry

def getGoogleMapForKrakow():

    KRAKOW_PRETTY_ZOOM = 12    
    gmap = GoogleMap(1200, 600)
    gmap.setCenter(Geocoder.getCoordinates("Krakow, Polska"))
    gmap.setZoom(KRAKOW_PRETTY_ZOOM)
    return gmap

def renderHtmlPage(gmap):
    print gmap.showHtml()

def run():

    gmap = getGoogleMapForKrakow()
    args = cgi.FieldStorage()
    querry = gumtreequerry.build(city='Krakow', whereabouts=args.getvalue("whereabouts", ""),
                                      numRooms=args.getvalue("numrooms", ""),
                                      minPrice=args.getvalue("minprice", ""),
                                      maxPrice=args.getvalue("maxprice", ""),
                                      minArea=args.getvalue("minarea", ""),
                                      maxArea=args.getvalue("maxarea", ""))

    offers = querryoffersource.getUrls(querry, int(args.getvalue("limit", 25)))
    points = OffersAsGooglePointsComposer.compose(offers)
    gmap.addPoints(points)
    renderHtmlPage(gmap)


reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

print "Content-type: text/html;charset=utf-8\n\n"

try:
    total_time = timeit.timeit(run, setup="gc.enable()", number=1)
except Exception, e:
    print "Exception: ", e
    
print "Time taken: ", total_time
print "Num active threads: ", threading.active_count()






