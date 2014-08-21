"""
This module must be imported before all others;
it is responsible for configuring the dependency injection controller
so that all the classes using injected dependencies are setup correctly
before they are first time used.
The configuration can be later reimplemented using some sort of config file
"""

from injectdependency import InjectDependency
from utf8printer import Utf8Printer
from geocoderwithcache import GeocoderWithCache
from urlfetcher import UrlFetcher
from addressresolver import AddressResolver
from wardrobe import Wardrobe
from parallelgumtreeofferfetcher import ParallelGumtreeOfferFetcher
from gumtreeofferurls import GumtreeOfferUrls

InjectDependency.setDependency('logger', '[logger here]')
InjectDependency.setDependency('printer', Utf8Printer)
InjectDependency.setDependency('urlfetcher', UrlFetcher)
InjectDependency.setDependency('offerfetcher', ParallelGumtreeOfferFetcher)
InjectDependency.setDependency('offerurls', GumtreeOfferUrls)
InjectDependency.setDependency('addressresolver', AddressResolver)

addressstorage = Wardrobe.fromFile('data/cachedaddresses.db')
InjectDependency.setDependency('geocoder', GeocoderWithCache(storage=addressstorage))

offerCache = Wardrobe.fromFile('data/cachedoffers.db')
InjectDependency.setDependency('offercache', offerCache)
