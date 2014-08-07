'''
Created on 03-08-2014

@author: mateusz
'''
from geocoder import Geocoder

class GeocoderWithCache():
    def __init__(self, geocoder=Geocoder, storage=dict()):
        self.geocoder = geocoder
        self.addressCache = storage
        
    def getCoordinates(self, address):
        address = self.normalize(address)
        if (self.cachedAddress(address)):
            return self.getCachedCoordsForAddress(address)
        else:
            return self.geocoder.getCoordinates(address)
            
    def registerAddress(self, address, coordinates):
        address = self.normalize(address)
        self.addressCache[address] = coordinates
        
    def normalize(self, address):
        return address.lower()
    
    def cachedAddress(self, address):
        return (address in self.addressCache)
    
    def getCachedCoordsForAddress(self, address):
        return self.addressCache[address]
        