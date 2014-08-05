'''
Created on 04-08-2014

@author: mateusz
'''
import unittest
from injectdependency import (Inject, DependencyInjectionException, InjectDependency)

    
# Register the dependency for testing purposes.
# This should be normally done in a common test environment module
InjectDependency.registerDependency('logger', "[DefaultLogger]")

class Test(unittest.TestCase):
    
    def testInjectAndChangeDependency(self):
        @InjectDependency('logger')
        class ObjectUnderTest():
            logger = Inject # mark field as designated for injecting with "Inject"
           
        # check properly injected
        self.assertEquals('[DefaultLogger]', ObjectUnderTest.logger) 
        
        # change dependency
        InjectDependency.changeDependency('logger', "[FunkyLogger]")
        
        # check properly changed
        self.assertEquals('[FunkyLogger]', ObjectUnderTest.logger)
                
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
        
    def testThrowsOnAlreadyRegistered(self):
        try:
            InjectDependency.registerDependency('logger', "[DefaultLogger]")
            self.fail("Should have failed on registering already registered dependency")
        except DependencyInjectionException:
            pass
        
    def testThrowsOnChangeNotRegistered(self):
        try:
            InjectDependency.changeDependency('unregistered_dependency', "Amba Fatima...!")
            self.fail("Should have failed on changing non registered dependency")
        except DependencyInjectionException:
            pass
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()