import time
import pstats
import setupdependencyinjection  # @UnusedImport setups dependency injection
import cProfile
from desktopview import DesktopView
from gumtreequerry import GumtreeQuerry
from gumtreeofferswithcache import GumtreeOffersWithCache
from injectdependency import InjectDependency, Inject

@InjectDependency('logger')
class Demo():
    logger = Inject
    
    @staticmethod
    def run():
        PROFILER_RAW = 'diagnostics/rawprofiler.bin'
        PROFILER_TXT = 'diagnostics/profiler.txt'
        try:
            Demo.logger.info("New session: " + time.strftime("%X, %x"))
            cProfile.run("Demo.runUnderDiagnosticsControl()", filename=PROFILER_RAW)
            p = pstats.Stats(PROFILER_RAW, stream=open(name=PROFILER_TXT, mode='a'))
            p.strip_dirs().sort_stats('cumulative').print_stats(20)
            
        except Exception, e:
            Demo.logger.exception(e)
            
        finally:
            Demo.logger.info(" Session done. " + time.strftime("%X") + "\n")   
         
    @staticmethod
    def runUnderDiagnosticsControl():
    
        print "Composing offer querry"
        querry = GumtreeQuerry.compose(city='Krakow')
        
        print "Fetching offers"
        offers = GumtreeOffersWithCache.askForOffers(querry, 8)
    
        print "Rendering the offer page"
        DesktopView.render(offers, querry.city)
        
        print "Done."
    
if (__name__ == "__main__"):
    Demo.run()