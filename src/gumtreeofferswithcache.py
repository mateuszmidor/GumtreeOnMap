'''
Created on 11-08-2014

@author: mateusz
'''

import setupdependencyinjection  # @UnusedImport setups dependency injection

from gumtreeofferurls import GumtreeOfferUrls
from injectdependency import InjectDependency, Inject

@InjectDependency('addressresolver', 'offercache', 'offerfetcher', 'offerurls')
class GumtreeOffersWithCache():
    offercache = Inject
    addressresolver = Inject
    offerfetcher = Inject
    offerurls = Inject
    
    @staticmethod
    def askForOffers(querry, count):
        # value limited by netmark host

        MAX_THREADS = 8 
        querryUrl = str(querry)
        urls = GumtreeOffersWithCache.offerurls.getUrls(querryUrl, count)
        cityAddressResolver = GumtreeOffersWithCache.addressresolver.forCity(querry.city)
        fetcher = GumtreeOffersWithCache.offerfetcher.parallelWithAddressResolutionAndGeocoding(cityAddressResolver, MAX_THREADS)
        return GumtreeOffersWithCache.getOffersFromUrls(urls, fetcher)
        
    @staticmethod
    def getOffersFromUrls(urls, fetcher):
        offercache = GumtreeOffersWithCache.offercache
        offers = []
        
        for url in urls:
            if (url in offercache):
                offers.append(offercache[url])
            else:
                fetcher.enqueueUrl(url)
         
        fetchedOffers = fetcher.offers()    
        GumtreeOffersWithCache.cacheOffers(fetchedOffers)         
        return offers + fetchedOffers 
    
    @staticmethod 
    def cacheOffers(offers):
        for offer in offers:
            url = offer["url"]
            GumtreeOffersWithCache.offercache[url] = offer