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
            self.knownAddresses = addressDict
        else:
            self.knownAddresses = shelve.open("data/geocodedaddresses.db")
        
    def getCoordinates(self, address):
        address = address.lower() # addresses in cache are encoded as lowercase
        if (self.knownAddress(address)):
            return self.getCachedCoordsForAddress(address)
        else:
            return self.geocoder.getCoordinates(address)
            
    def knownAddress(self, address):
        return (address in self.knownAddresses)
    
    def getCachedCoordsForAddress(self, address):
        return self.knownAddresses[address]
        