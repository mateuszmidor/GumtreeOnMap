import feedparser

def getOffers(*rssUrls):
    
    
    offers = []
    for url in rssUrls:
        feed = feedparser.parse(url)
        
        for item in feed["items"]:
            offer = {"title" : item["title"],
                     "summary" : item["summary"],
                     "link" : item["link"],
                     "date" : item["date"]}
            offers.append(offer)

    return offers
            
