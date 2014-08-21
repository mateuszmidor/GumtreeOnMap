# -*- coding: utf-8 -*-

import setupdependencyinjection  # @UnusedImport setups dependency injection controller

from gumtreequerry import GumtreeQuerry
from gumtreeoffers import GumtreeOffers
from onlineview import OnlineView
from src.injectdependency import InjectDependency, Inject

@InjectDependency('logger')
class Main():
    logger = Inject
    
    @staticmethod
    def run(params):
        try:
            querry = GumtreeQuerry.compose(city='Krakow', 
                                           whereabouts=params.getvalue("whereabouts", ""),
                                           numRooms=params.getvalue("numrooms", ""),
                                           minPrice=params.getvalue("minprice", ""),
                                           maxPrice=params.getvalue("maxprice", ""),
                                           minArea=params.getvalue("minarea", ""),
                                           maxArea=params.getvalue("maxarea", ""))
        
            offerCountLimit = int(params.getvalue("limit", 25))
            offers = GumtreeOffers.askForOffers(querry, offerCountLimit)
            OnlineView.render(offers, querry.city)
        except Exception, e:
            Main.logger.exception(e)