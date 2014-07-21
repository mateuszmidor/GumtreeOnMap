import urllib3 # for thread safety, urllib2 hangs the app
import re
import threading
import Queue
import gumtreeofferparser as parser

class HtmlFetcher:
    @staticmethod
    def fetch(url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        return unicode(r.data, "UTF-8")
    
class OfferFetcher(threading.Thread):
    def __init__(self, inQueue, outQueue):
        threading.Thread.__init__(self)
        self.inQueue = inQueue
        self.outQueue = outQueue

    def getOffer(self, url):
        html = HtmlFetcher.fetch(url)
        title = parser.extractTitle(html)
        date = parser.extractDate(html)
        price = parser.extractPrice(html)
        address = parser.extractAddress(html)
        description = parser.extractDescription(html)
        summary = parser.extractSummary(html)
        imageUrl = parser.extractImageUrl(html)
        offer = {"title" : title,
                 "date" : date,
                 "price" : price,
                 "address" : address,
                 "description" : description,
                 "summary" : summary,
                 "url" : url,
                 "imageUrl" : imageUrl}
        return offer
    
    def run(self):
        url = self.inQueue.get()       
        offer = self.getOffer(url)
        self.outQueue.put(offer)
        self.inQueue.task_done()



def extractUrlFromHtml(html):
    pattern = 'a href="([^"]*)'
    return re.search(pattern, html).group(1)

def extractOfferUrls(html):
    START_TAG = '<div class="ar-title">'
    STOP_TAG = '</div>'
    urls = set([])
    
    iStart = html.find(START_TAG)
    while (iStart != -1):
        iStop = html.find(STOP_TAG, iStart)

        # a href=http://...
        htmlLink = html[iStart + len(START_TAG):iStop]

        # http://...
        url = extractUrlFromHtml(htmlLink)
        urls.add(url)
        iStart = html.find(START_TAG, iStop)

    return urls

def getOffers(gumtreeQuerry):
    html = HtmlFetcher.fetch(gumtreeQuerry)
    urls = extractOfferUrls(html)
    
    inQueue = Queue.Queue()
    outQueue = Queue.Queue()

    # fetch offers in seperate threads
    for url in urls:
        t = OfferFetcher(inQueue, outQueue)
        t.setDaemon(True)
        t.start()
        inQueue.put(url)
        

    # wait for all pages to be processed
    print "Waiting for threads to finish processing pages..."
    inQueue.join()
    print "Finished"
    offers = []
    for i in range(len(urls)):
        offers.append(outQueue.get())
        
        
    return offers   
   
    
#--------------------------- DEMO
if (__name__ == "__main__"):
    querry = "http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/d%C4%99bniki/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&isSearchForm=true&maxPrice=1600&maxPriceBackend=160000"

    offers = getOffers(querry)
    FORMATTER = u"{0} - {1}, {2}\n{3}\n{4}\n{5}\n{6}\n"
    for offer in offers:
        print "*" * 20
        print FORMATTER.format(offer["title"],
                               offer["date"],
                               offer["price"],
                               offer["address"],
                               offer["summary"],
                               offer["imageUrl"],
                               offer["url"])

