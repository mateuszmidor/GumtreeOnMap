'''
Created on 03-08-2014

@author: mateusz
'''
from utf8printer import Utf8Printer

class HttpResponse():
    '''
    classdocs
    '''

    @staticmethod
    def renderPage(html, printer=Utf8Printer):
        HttpResponse.printHttpContentTypeHeader(printer) 
        HttpResponse.printContent(html, printer)  
             
    @staticmethod
    def printHttpContentTypeHeader(printer):
        printer.printText(u"Content-type: text/html;charset=utf-8\n\n")

    @staticmethod
    def printContent(html, printer):
        printer.printText(html)