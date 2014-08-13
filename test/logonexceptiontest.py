'''
Created on 10-08-2014

@author: mateusz
'''
import unittest
import setupdependencyinjectiontest  # @UnusedImport setups dependecny injection machine
from injectdependency import InjectDependency
from logonexception import LogOnException

class LoggerMock():
    @staticmethod
    def exception(exception, msg):
        LoggerMock.thrownExcept = exception
        LoggerMock.thrownMsg = msg

class Test(unittest.TestCase):

    def setUp(self):
        InjectDependency.setDependency('logger', LoggerMock)

    def testInterceptsAndLogs(self):
        EXCEPTION = Exception('SomeException')
        MESSAGE = 'AnExceptionThrown'
        
        # run the test
        @LogOnException(MESSAGE)
        def func():
            raise EXCEPTION
        
        func()
        
        # check the exception was properly logged
        self.assertEquals(EXCEPTION, LoggerMock.thrownExcept)
        self.assertEquals(MESSAGE, LoggerMock.thrownMsg)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()