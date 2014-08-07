'''
Created on 07-08-2014

@author: mateusz
'''
import shelve
import unidecode

class Wardrobe():
    """
    Kind of shelve that accepts unicode as keys
    """
    
    storage = None

    @staticmethod
    def fromDictionary(dictionary):
        wardrobe = Wardrobe({})
        for key, value in dictionary.items():
            wardrobe[key] = value 
        return wardrobe
    
    @staticmethod
    def fromFile(filename, writeback = False):
        storage = shelve.open(filename = filename, writeback = writeback)
        return Wardrobe(storage)
    
    def __init__(self, storage):
        self.storage = storage
     
    def __getitem__(self, unicodeName):
        name = self.unicodeToNearestAscii(unicodeName)
        return self.storage[name]
    
    def __setitem__(self, unicodeName, value):
        name = self.unicodeToNearestAscii(unicodeName)
        self.storage[name] = value
        
    def unicodeToNearestAscii(self, ustr):
        # here find the nearest representation of ustr in ascii
        return unidecode.unidecode(ustr)