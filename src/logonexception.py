'''
Created on 10-08-2014

@author: mateusz
'''
from injectdependency import InjectDependency, Inject

@InjectDependency('logger')
class LogOnException():
    logger = Inject
    def __init__(self, msg):
        self.thrownMsg = msg
        
    def __call__(self, func):
        def wrapper(*args):
            try:
                return func(*args)
            except Exception, e:
                LogOnException.logger.exception(e, self.thrownMsg)    
                
        return wrapper 