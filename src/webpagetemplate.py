'''
Created on 31-07-2014

@author: mateusz
'''
import codecs

class WebPageTemplate():
    __html = u""
    
    @staticmethod
    def fromFile(filename):
        html = codecs.open(filename, encoding="utf-8").read()
        return WebPageTemplate(html)
        
    @staticmethod
    def fromHtml(html):
        return WebPageTemplate(html)
    
    def __init__(self, html):
        self.__html = html
        
    def setField(self, fieldname, value):
        if (isinstance(value, str)):
            value = unicode(value, 'utf-8') # from string
        else:
            value = unicode(value) # from eg float, integer, etc
            
        self.__html = self.__html.replace(unicode(fieldname), value)
        
    def saveToFile(self, filename):
        codecs.open(filename, mode="wb", encoding="utf-8").write(self.__html)
        
    def getHtml(self):
        return self.__html