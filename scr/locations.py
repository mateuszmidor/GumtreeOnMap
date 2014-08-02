
class Locations:
    @staticmethod
    def fromOffers(offers):
        """ 
        Turns offer list into offers grouped by location: 
        locations['Wielicka 9'] =  {longlatt = [51.12, 11.19],
                                    offers = [...]}
        """
        
        locations = {}
        for offer in offers:
            address = offer["address"]
            longlatt = offer["longlatt"]
            del offer["address"]
            del offer["longlatt"]
            
            # no offer list at such address? create one
            if (address not in locations):
                locations[address] = {'longlatt' : longlatt,
                                      'offers' : []}
            
            # append offer at this address
            locations[address]['offers'].append(offer)

        return locations