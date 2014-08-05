'''
Created on 03-08-2014

@author: mateusz
'''
import shelve
from geocoder import Geocoder

class GeocoderWithCache():
    def __init__(self, addressDict = None, geocoder=Geocoder):
        self.geocoder = geocoder
        if (addressDict):
            self.cachedAddresses = addressDict
        else:
            self.cachedAddresses = shelve.open("data/geocodedaddresses.db")
        
    def getCoordinates(self, address):
        address = address.lower() # addresses in cache are encoded as lowercase
        if (self.cachedAddress(address)):
            return self.getCachedCoordsForAddress(address)
        else:
            return self.geocoder.getCoordinates(address)
            
    def cachedAddress(self, address):
        return (address in self.cachedAddresses)
    
    def getCachedCoordsForAddress(self, address):
        return self.cachedAddresses[address]
        