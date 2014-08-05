'''
Created on 01-08-2014

@author: mateusz
'''
import unittest
from webpagetemplate import WebPageTemplate

class Test(unittest.TestCase):
    def testSetField(self):
        SOURCE_HTML = "<HTML><HEAD><TITLE>$TITLE$</TITLE></HEAD></HTML>"
        page = WebPageTemplate.fromHtml(SOURCE_HTML)
        page.setField("$TITLE$", "WebPageTemplateTest")
        
        EXPECTED_HTML = "<HTML><HEAD><TITLE>WebPageTemplateTest</TITLE></HEAD></HTML>"
        self.assertEquals(EXPECTED_HTML, page.getHtml())