'''
Created on 03-08-2014

@author: mateusz
'''
from injectdependency import Inject, InjectDependency

@InjectDependency('printer')
class HttpResponse():
    printer = Inject
    
    @staticmethod
    def renderPage(html):
        HttpResponse.printHttpContentTypeHeader() 
        HttpResponse.printContent(html)  
             
    @staticmethod
    def printHttpContentTypeHeader():
        HttpResponse.printer.printText(u"Content-type: text/html;charset=utf-8\n\n")

    @staticmethod
    def printContent(html, ):
        HttpResponse.printer.printText(html)