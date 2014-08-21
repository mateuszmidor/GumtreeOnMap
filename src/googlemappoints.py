'''
Created on 31-07-2014

@author: mateusz
'''
import datetime
import cgi
class GoogleMapPoints():
    
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
    def fromLocations(locations):
        points = []
        for address, location in locations.items():
            hint = GoogleMapPoints.prepareHintHeader(address)

            # there can be many offers at single location eg many flats on one street
            for offer in location["offers"]:
                addressSection = offer["addressSection"]
                title = offer["title"]
                date = offer["date"]
                price = offer["price"]
                url = offer["url"]
                summary = offer["summary"]
                hint = hint + GoogleMapPoints.prepareHintBody(title, date, price, addressSection, summary, url)
                
            hint = hint.replace("'", "&apos;")
            longitude, lattitude = location["longlatt"]
            iconName = GoogleMapPoints.getIconForDate(date)
            point = [longitude, lattitude, hint, iconName]
            points.append(point)
        
        return GoogleMapPoints(points)
    
    def __init__(self, points):
        self.points = points
        
    def removeNewlines(self, s):
        return s.replace(u'\n', u'').replace(u'\r', u'')
    
    def asJavaScript(self):
        """ [[50.11, 10.54, 'Nowe mieszkanie w centrum...', icon_today], [...]] """
        
        stringPoints = []
        for point in self.points:
            s = u"[{0}, {1}, '{2}', {3}]".format(point[0], point[1], point[2], point[3])
            stringPoints.append(s) 
            
        js = u"[" + ", ".join(stringPoints) + "]"
        return self.removeNewlines(js)