'''
Created on 03-08-2014

@author: mateusz
'''
#-----------------------------------------------------------------------------------------------
# First prepare DI controller for injecting dependencies
class FakePrinter():
    printedTextSequence = []
    
    @staticmethod
    def printText(text):
        FakePrinter.printedTextSequence.append(text)
      
from injectdependency import InjectDependency
InjectDependency.registerDependency('printer', FakePrinter)



#-----------------------------------------------------------------------------------------------
# Then rest of unit test
import unittest
from httpresponse import HttpResponse

class Test(unittest.TestCase):
        
    def testRenderPage(self):
        HTTP_CONTENT_TYPE_HEADER = u"Content-type: text/html;charset=utf-8\n\n"
        CONTENT = u"<HTML><HEAD><TITLE>SamplePage</Title></HEAD></HTML>"
        printer = FakePrinter
        
        HttpResponse.renderPage(CONTENT)
        
        self.assertEquals(HTTP_CONTENT_TYPE_HEADER, printer.printedTextSequence[0])
        self.assertEquals(CONTENT, printer.printedTextSequence[1])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRenderPage']
    unittest.main()