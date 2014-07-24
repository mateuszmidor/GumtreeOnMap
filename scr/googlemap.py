from pymaps import *

class GoogleMap:
    # map = None
    def __init__(self, widthInPixels = 500, heightInPixels = 300):
        g = PyMap()                         # creates an icon & map by default

        icon_today = Icon('icon_today')               # create an additional icon
        icon_today.image = "http://labs.google.com/ridefinder/images/mm_20_red.png" # for testing only!
        icon_today.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png" # do not hotlink from your web page!

        icon_older = Icon('icon_older')               # create an additional icon
        icon_older.image = "http://labs.google.com/ridefinder/images/mm_20_blue.png" # for testing only!
        icon_older.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png" # do not hotlink from your web page!
     

        g.addicon(icon_today)
        g.addicon(icon_older)
        g.key = "ABQIAAAAQQRAsOk3uqvy3Hwwo4CclBTrVPfEE8Ms0qPwyRfPn-DOTlpaLBTvTHRCdf2V6KbzW7PZFYLT8wFD0A" # you will get your own key
        g.width = "{0}px".format(widthInPixels)
        g.height = "{0}px".format(heightInPixels)

        # default zoom and center values
        
        self.map = g

    def setCenter(self, coords):
        self.map.maps[0].center = coords

    def setZoom(self, zoom):
        self.map.maps[0].zoom = zoom
        
    def addPoint(self, point):
        self.map.maps[0].setpoint(point)

    def addPoints(self, points):
        for point in points:
            self.addPoint(point)
            
    def showHtml(self):
        return self.map.showhtml()
