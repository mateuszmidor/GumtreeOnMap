# -*- coding: utf-8 -*-

import setupdependencyinjection  # @UnusedImport setups dependency injection controller

import time
from gumtreequerry import GumtreeQuerry
from gumtreeoffers import GumtreeOffers
from onlineview import OnlineView
from injectdependency import InjectDependency, Inject
import cProfile
import pstats

@InjectDependency('logger')
class Main():
    logger = Inject
    
    @staticmethod
    def run(params):
        PROFILER_RAW = 'diagnostics/rawprofiler.bin'
        PROFILER_TXT = 'diagnostics/profiler.txt'
        try:
            Main.logger.info("New session: " + time.strftime("%X, %x"))
            cProfile.run("Main.runUnderDiagnosticsControl(params)", filename=PROFILER_RAW)
            p = pstats.Stats(PROFILER_RAW, stream=open(name=PROFILER_TXT, mode='a'))
            p.strip_dirs().sort_stats('time').print_stats(20)
            
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
    
        offerCountLimit = int(params.getvalue("limit", 25))
        offers = GumtreeOffers.askForOffers(querry, offerCountLimit)
        OnlineView.render(offers, querry.city)
