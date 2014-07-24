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

        
        addresses = {}
        for offer in items:
            title = offer["title"]
            date = offer["date"]
            price = offer["price"]
            addressSection = offer["addressSection"]
            address = offer["address"]
            lonlat = offer["lonlat"][0]
            summary = offer["summary"]
            description = offer["description"]
            imageUrl = offer["imageUrl"]
            url = offer["url"]



            """
            print "----------------------------------"
            print "Title\n", title
            print "Given address\n",addressSection
            print "Summary\n",summary
            print "Extracted address\n",address
            #print url
            print ""
            
      """
            # no offer list at such address? create one
            if (address not in addresses):
                addresses[address] = []
            
            # append offer at this address
            addresses[address].append({"addressSection" : addressSection,
                                       "lonlat" : lonlat,
                                       "summary" : summary,
                                       "title" :  title,
                                       "date" : date,
                                       "price" : price,
                                       "link" : url})

           
                     
                        
           
        return addresses
            
    @staticmethod
    def compose(items):
        
        addresses = OffersAsGooglePointsComposer.composeOffersByAddresses(items)
        points = []
        for address in addresses:
            hint = OffersAsGooglePointsComposer.prepareHintHeader(address)

            # there can be many offers at single address eg many flats on one street
            for offer in addresses[address]:
                addressSection = offer["addressSection"]
                title = offer["title"]
                date = offer["date"]
                price = offer["price"]
                link = offer["link"]
                summary = offer["summary"]
                hint = hint + OffersAsGooglePointsComposer.prepareHintBody(title, date, price, addressSection, summary, link)
                lon, latt =   offer["lonlat"]
            iconName = OffersAsGooglePointsComposer.getIconForDate(date)
            point = [lon, latt, hint, iconName]
            points.append(point)

        return points
