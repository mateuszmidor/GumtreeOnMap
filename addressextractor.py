# -*- coding: utf-8 -*-
import codecs
import re
class AddressExtractor:
    addresses = {}

    def loadAddresses(self, filename):
        with codecs.open(filename, encoding="utf-8") as f:
            # remove newline and make street name lowercase
            addresses = [address.replace("\r\n", "").lower() for address in f]

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
                    f = re.match(address + r' \d*\\?\d*', source)
                    if (f):
                        return f.group(0)

#--------------------------- DEMO
if (__name__ == "__main__"):
    extractor = AddressExtractor("streets.txt")
    print extractor.extract(u"Ludomira Różyckiego 5")
