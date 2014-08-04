'''
Created on 04-08-2014

@author: mateusz
'''
import unittest
from injectdependency import (Inject, DependencyInjectionException, InjectDependency)
    
class Test(unittest.TestCase):
    def __init__(self, methodname):
        unittest.TestCase.__init__(self, methodname)
        # dependency must be registered before can be used
        InjectDependency.registerDependency('logger', '[LoggerInstance]')
    
    def testInjectDependency(self):
        @InjectDependency('logger')
        class ObjectUnderTest():
            logger = Inject # mark field as designated for injecting with "Inject"
            
        instance = ObjectUnderTest()
        self.assertEquals('[LoggerInstance]', instance.logger)
        
    def testThrowsOnInjectingUnregisteredDependency(self):
        try:
            @InjectDependency('unregistered_dependency')
            class ObjectUnderTest():
                unregistered_dependency = Inject # unregistered_dependency is not registered
                
            self.fail("Should have thrown on using unregistered dependency")
        except DependencyInjectionException:
            pass

    def testThrowsOnNoSuchField(self):
        try:
            @InjectDependency('logger')
            class ObjectUnderTest():
                LOGGER = Inject # 'LOGGER' != 'logger'
                
            self.fail("Should have thrown on injecting into non-existing field")
        except DependencyInjectionException:
            pass
        
    def testThrowsOnNonInjectionDesignatedField(self):
        try:
            @InjectDependency('logger')
            class ObjectUnderTest():
                logger = None # logger not marked with 'Inject'   
                
            self.fail("Should have thrown on injecting into field not marked for injection")
        except DependencyInjectionException:
            pass
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()