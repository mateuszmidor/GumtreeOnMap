import pygeocoder 

class Geocoder:
    @staticmethod
    def getCoordinates(address):
        return pygeocoder.Geocoder.geocode(address)[0].coordinates
