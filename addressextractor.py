# -*- coding: utf-8 -*-
import codecs
import re
class AddressExtractor:
    addresses = {}

    def loadAddresses(self, filename):
        with codecs.open(filename, encoding="utf-8") as f:
            addresses = []
            # remove newline and make street name lowercase
            for line in f:
                address = line.strip("\n\r\t ").lower()
                if (address != ""):
                    addresses.append(address)           

        # longest first - for 'find' to match Krakowska before Krakow
        addresses.sort(lambda s1, s2: cmp(len(s2), len(s1)))
        return addresses

    def __init__(self, addressesFilename):
        self.addresses = self.loadAddresses(addressesFilename)


    
    def extract(self, *descriptions):
        """ This function needs some speedup"""
        for source in descriptions:
            source = source.lower()
            for address in self.addresses:
           
                if (source.find(address)) != -1:
                    # can be followed by a number
                    f = re.search(address + r"\s*\d*", source)
                    if (f):
                        return f.group(0)
        
        return None

#--------------------------- DEMO
if (__name__ == "__main__"):
    extractor = AddressExtractor("districts.txt")
    print extractor.extract(u"Mieszkanie Mydlniki")
