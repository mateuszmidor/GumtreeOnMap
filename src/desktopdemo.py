# -*- coding: utf-8 -*-

import timeit

import setupdependencyinjection  # @UnusedImport setups dependency injection

from desktopview import DesktopView
from gumtreequerry import GumtreeQuerry
from gumtreeoffers import GumtreeOffers

def run():

    print "Composing offer querry"
    querry = GumtreeQuerry.compose(city='Krakow' )

    print "Fetching offers"
    offers = GumtreeOffers.askForOffers(querry, 20)

    print "Rendering the offer page"
    DesktopView.render(offers, querry.city)
    
    print "Done."
    

total_time = timeit.timeit(run, setup="gc.enable()", number=1)
print "Time taken: ", total_time