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
     
    def __contains__(self, unicodeKey):
        key = self.ensureAscii(unicodeKey)
        return (key in self.storage)
     
    def __getitem__(self, unicodeName):
        name = self.ensureAscii(unicodeName)
        return self.storage[name]
    
    def __setitem__(self, unicodeName, value):
        name = self.ensureAscii(unicodeName)
        self.storage[name] = value
        
    def ensureAscii(self, s):
        # here find the nearest representation of s in ascii
        if isinstance(s, unicode):
            return unidecode.unidecode(s)
        else:
            return s