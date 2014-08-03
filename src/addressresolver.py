'''
Created on 31-07-2014

@author: mateusz
'''
from addressextractor import AddressExtractor


streetExtractor = AddressExtractor("data/streets.txt")
districtExtractor = AddressExtractor("data/districts.txt")

class AddressResolver():
    '''
    classdocs
    '''
    
    # this country will be added as suffix to every returned address
    OPERATING_COUNTRY = u"polska"
    
    @staticmethod
    def resolve(cityToLookForTheAddressIn, *sources):
        # this is the first place to speedup; longers from 4 -> 10 sec/25offer
        # introduce offer cache?
        address = streetExtractor.extract(*sources)

        if (not address):
            address = districtExtractor.extract(*sources)
            
        return AddressResolver.formFullAddress(address, cityToLookForTheAddressIn)

    @staticmethod
    def formFullAddress(address, cityToLookForTheAddressIn):
        # TODO:  City extractor
        if (not address):
            #address = cityExtractor.extract(addressSection, title, summary)
            return "%s, %s" % (cityToLookForTheAddressIn, AddressResolver.OPERATING_COUNTRY)
        else:
            return "%s, %s, %s" % (address, cityToLookForTheAddressIn, AddressResolver.OPERATING_COUNTRY)
    
    
