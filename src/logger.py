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
        logging.basicConfig(filename=filename,level=logging.INFO)
        
    def exception(self, e):
        logging.exception(str(e))
        
    def debug(self, msg):
        logging.debug(msg)
        
    def info(self, msg):
        logging.info(msg)
        
    def warn(self, msg):
        logging.warn(msg)
        
    def error(self, msg):
        logging.error(msg)