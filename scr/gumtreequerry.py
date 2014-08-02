class GumtreeQuerry:
    __TEMPLATE = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/{_city}/{_whereabouts}c9008l3200208?A_AreaInMeters_max={_maxArea}&A_AreaInMeters_min={_minArea}&A_ForRentBy=ownr&A_NumberRooms={_numRooms}&AdType=2&isSearchForm=true&maxPrice={_maxPrice}&maxPriceBackend=200000&minPrice={_minPrice}&minPriceBackend=100000'
    
    @staticmethod
    def compose(city = "", whereabouts = "", numRooms = "", minPrice = "", maxPrice = "", minArea = "", maxArea = ""):
        # city is obligatory
        if (not city):
            raise ValueError("city is obligatory to compose a valid querry")
        
        # ensure spaces are encoded as '+'signs
        # whereabouts is an address element, not param, so must end with '/' if provided
        if (whereabouts != ""):
            whereabouts = whereabouts.replace(' ', '+') + '/'
            
        # gumtree encodes one room as '10'
        if (numRooms == "1"):
            numRooms = "10" 
        
        querry = GumtreeQuerry.__TEMPLATE.format(_city = city, _whereabouts = whereabouts, _numRooms = numRooms, 
                                               _minPrice = minPrice, _maxPrice = maxPrice, _minArea = minArea, 
                                               _maxArea = maxArea)
        return querry
