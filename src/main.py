# -*- coding: utf-8 -*-

import setupdependencyinjection  # @UnusedImport setups dependency injection controller

import time
import cProfile
import pstats
from gumtreequerry import GumtreeQuerry
from onlineview import OnlineView
from injectdependency import InjectDependency, Inject
from gumtreeofferswithcache import GumtreeOffersWithCache

@InjectDependency('logger')
class Main():
    logger = Inject
    
    @staticmethod
    def run(params):
        PROFILER_RAW = 'diagnostics/rawprofiler.bin'
        PROFILER_TXT = 'diagnostics/profiler.txt'
        try:
            Main.logger.info("New session: " + time.strftime("%X, %x"))
            
            if ("profile" in params):
                args = params # weird trick for "undefined variable: params" @UnusedVariable
                cProfile.run("Main.runUnderDiagnosticsControl(args)", filename=PROFILER_RAW)
                p = pstats.Stats(PROFILER_RAW, stream=open(name=PROFILER_TXT, mode='a'))
                p.strip_dirs().sort_stats('time').print_stats(20)
            else:
                Main.runUnderDiagnosticsControl(params)
            
        except Exception, e:
            Main.logger.exception(e)
            
        finally:
            Main.logger.info("Session done. " + time.strftime("%X") + "\n")         
        
    @staticmethod
    def runUnderDiagnosticsControl(params):
        querry = GumtreeQuerry.compose(city='Krakow', 
                                       whereabouts=params.getvalue("whereabouts", ""),
                                       numRooms=params.getvalue("numrooms", ""),
                                       minPrice=params.getvalue("minprice", ""),
                                       maxPrice=params.getvalue("maxprice", ""),
                                       minArea=params.getvalue("minarea", ""),
                                       maxArea=params.getvalue("maxarea", ""))
    
        offerCountLimit = int(params.getvalue("limit", 24))
        offers = GumtreeOffersWithCache.askForOffers(querry, offerCountLimit)
        OnlineView.render(offers, querry.city)
