import pygeocoder 

class Geocoder:
    API_KEY = "AIzaSyAnelYhxyAsoYVLUouQ4pt7q9tlt4NunI0" # for 3demaniac account
    geocoder = pygeocoder.Geocoder(API_KEY)
#     lock = PeriodicLock(0.1) # 100 ms to conform google geocoding limit between subsequent geocodes
    
    @staticmethod
    def getCoordinates(address):
#         Geocoder.lock.wait() # seems not needed when using geocoder with API key
        return Geocoder.geocoder.geocode(address)[0].coordinates