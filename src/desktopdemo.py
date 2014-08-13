# -*- coding: utf-8 -*-

import setupdependencyinjection  # @UnusedImport setups dependency injection

import cProfile
from desktopview import DesktopView
from gumtreequerry import GumtreeQuerry
from gumtreeofferswithcache import GumtreeOffersWithCache

def run():

    print "Composing offer querry"
    querry = GumtreeQuerry.compose(city='Krakow')
    
    print "Fetching offers"
    offers = GumtreeOffersWithCache.askForOffers(querry, 5)

    print "Rendering the offer page"
    DesktopView.render(offers, querry.city)
    
    print "Done."
    

cProfile.run('run()', sort='cumulative')
# total_time = timeit.timeit(run, setup="gc.enable()", number=1)
# print "Time taken: ", total_time