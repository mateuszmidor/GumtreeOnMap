'''
Created on 03-08-2014

@author: mateusz
'''
from geocoder import Geocoder
from injectdependency import InjectDependency, Inject


@InjectDependency('logger')
class GeocoderWithCache():
    logger = Inject
    
    def __init__(self, geocoder=Geocoder, storage=dict()):
        self.geocoder = geocoder
        self.addressCache = storage
        
    def getCoordinates(self, address):
        address = self.normalize(address)
        if (self.cachedAddress(address)):
            return self.getCachedCoordsForAddress(address)
        else:
            coordinates =  self.geocoder.getCoordinates(address)
            self.addressCache[address] = coordinates
            return coordinates
            
    def registerAddress(self, address, coordinates):
        address = self.normalize(address)
        self.addressCache[address] = coordinates
        self.logger.info("Registered new address: " + address + " " + str(coordinates))
        
    def normalize(self, address):
        return address.lower()
    
    def cachedAddress(self, address):
        return (address in self.addressCache)
    
    def getCachedCoordsForAddress(self, address):
        coordinates = self.addressCache[address]
        self.logger.info("Fetched address from cache: " + address + " " + str(coordinates))
        return coordinates
        