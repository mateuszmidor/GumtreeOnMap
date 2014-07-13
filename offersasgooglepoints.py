from addressextractor import AddressExtractor
from geocoder import Geocoder
import datetime
class OffersAsGooglePointsComposer:

    @staticmethod
    def prepareHintHeader(address):
        FORMATTER = u'<b>{0}</b></br>'
        return FORMATTER.format(address)

    @staticmethod
    def prepareHintBody(title, date, price, addressSection, summary, url):
        FORMATTER = u'{0} - {1} <b>{2}</b></br><i>{3}</i></br>{4}</br><a href="{5}" target="_blank">Link</a></br>'
        return FORMATTER.format(title, date, price, addressSection, summary, url)

    @staticmethod
    def getIconForDate(gumtreeDate):
        now = datetime.datetime.now()
        gumtreeFormatNow = now.strftime("%d/%m/%Y")
        if (gumtreeDate == gumtreeFormatNow):
            return 'icon_today'
        else:
            return 'icon_older'

    @staticmethod
    def composeOffersByAddresses(items):
        streetExtractor = AddressExtractor("streets.txt")

        addresses = {}
        for offer in items:
            title = offer["title"]
            date = offer["date"]
            price = offer["price"]
            addressSection = offer["address"]
            summary = offer["summary"]
            description = offer["description"]
            imageUrl = offer["imageUrl"]
            url = offer["url"]

            address = streetExtractor.extract(addressSection, title, summary)

            #not found
            if (not address):
                address = "Krakow"

            print "----------------------------------"
            print title
            print addressSection
            print summary
            print address
            print url
        
      
            # no offer list at such address? create one
            if (address not in addresses):
                addresses[address] = []

            # append offer at this address
            addresses[address].append({"addressSection" : addressSection,
                                       "summary" : summary,
                                       "title" :  title,
                                       "date" : date,
                                       "price" : price,
                                       "link" : url})

           
                     
                        
            print ""
        return addresses
            
    @staticmethod
    def compose(items):
        
        addresses = OffersAsGooglePointsComposer.composeOffersByAddresses(items)
        points = []
        for address in addresses:
            hint = OffersAsGooglePointsComposer.prepareHintHeader(address)
            lon, latt = Geocoder.getCoordinates(address + ", Krakow, Polska")

            for offer in addresses[address]:
                addressSection = offer["addressSection"]
                title = offer["title"]
                date = offer["date"]
                price = offer["price"]
                link = offer["link"]
                summary = offer["summary"]
                hint = hint + OffersAsGooglePointsComposer.prepareHintBody(title, date, price, addressSection, summary, link)

            iconName = OffersAsGooglePointsComposer.getIconForDate(date)
            point = [lon, latt, hint, iconName]
            points.append(point)

        return points
