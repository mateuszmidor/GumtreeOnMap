'''
Created on 29-08-2014

@author: mateusz
'''
import shelve

class FileStorage():

    def __init__(self, filename):
        self.storage = shelve.open(filename = filename, writeback = True)
        
    def __contains__(self, key):
        return (key in self.storage)
     
    def __getitem__(self, key):
        return self.storage[key]
    
    def __setitem__(self, key, value):
        self.storage[key] = value  
        self.storage.sync()