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
    @staticmethod
    def resolve(defaulAddress, *sources):
        # this is the first place to speedup; longers from 4 -> 10 sec/25offer
        # introduce offer cache?
        address = streetExtractor.extract(*sources)

        if (not address):
            address = districtExtractor.extract(*sources)
            
        # TODO:  City extractor
        if (not address):
            #address = cityExtractor.extract(addressSection, title, summary)
            address = defaulAddress
            
        return address.strip()
        