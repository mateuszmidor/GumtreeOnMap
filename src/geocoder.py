import pygeocoder 
from injectdependency import InjectDependency, Inject
from periodiclock import PeriodicLock

class Geocoder:
    lock = PeriodicLock(0.11) # 110 ms to conform google geocoding limit between subsequent geocodes
    
    @staticmethod
    def getCoordinates(address):
        Geocoder.lock.wait()
        return pygeocoder.Geocoder.geocode(address)[0].coordinates