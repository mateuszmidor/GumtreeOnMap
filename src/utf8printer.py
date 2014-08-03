'''
Created on 03-08-2014

@author: mateusz
'''
import sys
import codecs

class Utf8Printer():
    @staticmethod
    def setupUtf8Printing():
        reload(sys)
        sys.setdefaultencoding('utf-8')
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
        
    @staticmethod
    def printText(utf8Text):
        Utf8Printer.setupUtf8Printing()
        print utf8Text