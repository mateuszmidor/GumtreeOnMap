'''
Created on 04-08-2014

@author: mateusz
'''
import unittest
from injectdependency import Inject, DependencyInjectionException, InjectDependency

    
# Register examplary dependencies for testing purposes.
# This will be normally done in a SetupDependencyInjection module
InjectDependency.registerDependency('_testdb_', "[DefaultDB]")
InjectDependency.registerDependency('_testlogger_', "[DefaultLogger]")

class Test(unittest.TestCase):
    
    def testInjectDependency(self):
        @InjectDependency('_testdb_')
        class Object():
            _testdb_ = Inject
        
        # check if proper value injected
        self.assertEquals("[DefaultDB]", Object._testdb_)   
            
    def testChangeDependency(self):
        @InjectDependency('_testlogger_')
        class Object():
            _testlogger_ = Inject
            
        # check properly injected
        self.assertEquals('[DefaultLogger]', Object._testlogger_) 
        
        # change dependency
        InjectDependency.changeDependency('_testlogger_', "[FunkyLogger]")
        
        # check properly changed
        self.assertEquals('[FunkyLogger]', Object._testlogger_)
                
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
            @InjectDependency('_testlogger_')
            class Object():
                LOGGER = Inject # 'LOGGER' != '_testlogger_'
                
            self.fail("Should have thrown on injecting into non-existing field")
        except DependencyInjectionException:
            pass
        
    def testThrowsOnNonInjectionDesignatedField(self):
        try:
            @InjectDependency('_testlogger_')
            class Object():
                _testlogger_ = None # _testlogger_ not marked with 'Inject'   
                
            self.fail("Should have thrown on injecting into field not marked for injection")
        except DependencyInjectionException:
            pass
        
    def testThrowsOnAlreadyRegistered(self):
        try:
            InjectDependency.registerDependency('_testlogger_', "[DefaultLogger]")
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