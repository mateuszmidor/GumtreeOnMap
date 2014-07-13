import codecs

class AddressExtractor:
    addresses = []

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
        for source in descriptions:
            source = source.lower()
            for address in self.addresses:
                if (source.find(address)) != -1:
                    return address
            
