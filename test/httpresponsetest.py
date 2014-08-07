'''
Created on 03-08-2014

@author: mateusz
'''
import unittest
import setupdependencyinjectiontest  # @UnusedImport setups dependency injection forObject tests
from httpresponse import HttpResponse
from injectdependency import InjectDependency

# This guy is used by HttpResponse.renderPage
class FakePrinter():
    printedTextSequence = []
    
    @staticmethod
    def printText(text):
        FakePrinter.printedTextSequence.append(text)
      

class Test(unittest.TestCase):
        
    def setUp(self):
        InjectDependency.changeDependency('printer', FakePrinter)
         
    def testRenderPage(self):
        HTTP_CONTENT_TYPE_HEADER = u"Content-type: text/html;charset=utf-8\n\n"
        CONTENT = u"<HTML><HEAD><TITLE>SamplePage</Title></HEAD></HTML>"
        
        HttpResponse.renderPage(CONTENT)
        
        printer = FakePrinter # static class, so makes sense
        self.assertEquals(HTTP_CONTENT_TYPE_HEADER, printer.printedTextSequence[0])
        self.assertEquals(CONTENT, printer.printedTextSequence[1])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRenderPage']
    unittest.main()