'''
Created on 21-08-2014

@author: mateusz
'''
import logging

class Logger():

    @classmethod
    def toFile(cls, filename):
        return cls(filename)
    
    def __init__(self, filename):
        logging.basicConfig(filename=filename,level=logging.DEBUG)
        
    def exception(self, e):
        logging.exception(str(e))