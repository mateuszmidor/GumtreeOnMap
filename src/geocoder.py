import pygeocoder 

class Geocoder:
    @staticmethod
    def getCoordinates(address):
        return pygeocoder.Geocoder.geocode(address)[0].coordinates


if (__name__ == "__main__") :
    address = "Krakow, Poland"
    longitude, latitude = Geocoder.getCoordinates(address)
    print "%s:" % address
    print "longitude %f" % longitude
    print "latitude %f" % latitude
