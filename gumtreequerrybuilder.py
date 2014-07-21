TEMPLATE = 'http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/{_city}/{_whereabouts}c9008l3200208?A_AreaInMeters_max={_maxArea}&A_AreaInMeters_min={_minArea}&A_ForRentBy=ownr&A_NumberRooms={_numRooms}&AdType=2&isSearchForm=true&maxPrice={_maxPrice}&maxPriceBackend=200000&minPrice={_minPrice}&minPriceBackend=100000&Page='

def build(city = "", whereabouts = "", numRooms = "", minPrice = "", maxPrice = "", minArea = "", maxArea = ""):
    if (whereabouts != ""):
        whereabouts = whereabouts.replace(' ', '+') + '/'
    if (numRooms == "1"):
        numRooms = "10" # kawalerka
    
    querry = TEMPLATE.format(_city = city, _whereabouts = whereabouts, _numRooms = numRooms, _minPrice = minPrice, _maxPrice = maxPrice,
                           _minArea = minArea, _maxArea = maxArea)
    print querry
    return querry
