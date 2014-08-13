'''
Created on 04-08-2014

@author: mateusz
'''
import unittest
from injectdependency import Inject, DependencyInjectionException, InjectDependency

class Test(unittest.TestCase):
    
    def testInjectDependency(self):
        InjectDependency.setDependency('_testdb_', "[DefaultDB]")
        
        @InjectDependency('_testdb_')
        class Object():
            _testdb_ = Inject
        
        # check if proper value injected
        self.assertEquals("[DefaultDB]", Object._testdb_)   
            
    def testChangeDependency(self):
        InjectDependency.setDependency('_testlogger_', "[DefaultLogger]")
        
        @InjectDependency('_testlogger_')
        class Object():
            _testlogger_ = Inject
            
        # check properly injected
        self.assertEquals('[DefaultLogger]', Object._testlogger_) 
        
        # change dependency
        InjectDependency.setDependency('_testlogger_', "[FunkyLogger]")
        
        # check properly changed
        self.assertEquals('[FunkyLogger]', Object._testlogger_)
            

    def testInjectUnregisteredThenSetDependency(self):
        # inject unregistered dependency
        @InjectDependency('_testresourcemanager_')
        class Object():
            _testresourcemanager_ = Inject 
        
        # register the dependency
        InjectDependency.setDependency('_testresourcemanager_', "[FunkyResManager]")        
        
        # check properly changed
        self.assertEquals('[FunkyResManager]', Object._testresourcemanager_)
       
    def testManualInject(self):
        @InjectDependency('_testsetmanual_')
        class Object():
            _testsetmanual_ = Inject   
            
        # do manual injection
        InjectDependency.manualInject('_testsetmanual_', '[ManualSetSuccessful]', Object)      
        
        # check properly changed
        self.assertEquals('[ManualSetSuccessful]', Object._testsetmanual_)
        
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
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()