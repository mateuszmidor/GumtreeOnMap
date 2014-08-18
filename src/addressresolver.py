'''
Created on 31-07-2014

@author: mateusz
'''
from addressextractor import AddressExtractor

class AddressResolver():
    
    # this country will be added as suffix to every returned address
    OPERATING_COUNTRY = u"Polska"
    
    @classmethod
    def forCity(cls, city):
        streetExtractor = AddressExtractor("data/{0}_streets.txt".format(city))
        districtExtractor = AddressExtractor("data/{0}_districts.txt".format(city))   
        return cls(city, streetExtractor, districtExtractor)
    
    def __init__(self, city, streetExtractor, districtExtractor):
        self.city = city
        self.streetExtractor = streetExtractor 
        self.districtExtractor = districtExtractor    
    
    def resolve(self, *sources):
        # this is the first place to speedup; longers from 4 -> 10 sec/25offer
        # introduce offer cache?
        address = self.streetExtractor.extract(*sources)

        if (not address):
            address = self.districtExtractor.extract(*sources)
            
        return self.formFullAddress(address)

    def formFullAddress(self, address):
        # TODO:  City extractor
        if (not address):
            #address = cityExtractor.extract(addressSection, title, summary)
            return "%s, %s" % (self.city, AddressResolver.OPERATING_COUNTRY)
        else:
            return "%s, %s, %s" % (address, self.city, AddressResolver.OPERATING_COUNTRY)