#!/usr/bin/python

# -*- coding: utf-8 -*-

import setupdependencyinjection  # @UnusedImport setups dependency injection controller

import cgi
import timeit
from gumtreequerry import GumtreeQuerry
from gumtreeoffers import GumtreeOffers
from onlineview import OnlineView


def run():
    args = cgi.FieldStorage()
    querry = GumtreeQuerry.compose(city='Krakow', 
                                   whereabouts=args.getvalue("whereabouts", ""),
                                   numRooms=args.getvalue("numrooms", ""),
                                   minPrice=args.getvalue("minprice", ""),
                                   args.getvalue("maxprice", ""),
                                   minArea=args.getvalue("minarea", ""),
                                   maxArea=args.getvalue("maxarea", ""))

    offerCountLimit = int(args.getvalue("limit", 25))
    offers = GumtreeOffers.askForOffers(querry, offerCountLimit)
    OnlineView.render(offers, querry.city)

try:
    total_time = timeit.timeit(run, setup="gc.enable()", number=1)
except Exception, e:
    print "Exception: ", e
    
print "Time taken: ", total_time




