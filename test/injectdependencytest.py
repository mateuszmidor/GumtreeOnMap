'''
Created on 04-08-2014

@author: mateusz
'''
import unittest
from injectdependency import Inject, DependencyInjectionException, InjectDependency

    
# Register examplary dependencies for testing purposes.
# This will be normally done in a SetupDependencyInjection module
InjectDependency.registerDependency('db', "[DefaultDB]")
InjectDependency.registerDependency('logger', "[DefaultLogger]")

class Test(unittest.TestCase):
    
    def testInjectDependency(self):
        @InjectDependency('db')
        class Object():
            db = Inject
        
        # check if proper value injected
        self.assertEquals("[DefaultDB]", Object.db)   
            
    def testChangeDependency(self):
        @InjectDependency('logger')
        class Object():
            logger = Inject
            
        # check properly injected
        self.assertEquals('[DefaultLogger]', Object.logger) 
        
        # change dependency
        InjectDependency.changeDependency('logger', "[FunkyLogger]")
        
        # check properly changed
        self.assertEquals('[FunkyLogger]', Object.logger)
                
    def testThrowsOnInjectingUnregisteredDependency(self):
        try:
            @InjectDependency('unregistered_dependency')
            class Object():
                unregistered_dependency = Inject # unregistered_dependency is not registered
                
            self.fail("Should have thrown on using unregistered dependency")
        except DependencyInjectionException:
            pass

    def testThrowsOnNoSuchField(self):
        try:
            @InjectDependency('logger')
            class Object():
                LOGGER = Inject # 'LOGGER' != 'logger'
                
            self.fail("Should have thrown on injecting into non-existing field")
        except DependencyInjectionException:
            pass
        
    def testThrowsOnNonInjectionDesignatedField(self):
        try:
            @InjectDependency('logger')
            class Object():
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