'''
Created on 24-08-2014

@author: mateusz
'''
import time
from threading import Lock
from injectdependency import InjectDependency, Inject

@InjectDependency('logger')
class PeriodicLock():
    logger = Inject

    def __init__(self, period):
        self.period = period
        self.lock = Lock()
        self.lastTimeAcquired = -100.0 # never acquired
        
    def wait(self):
        self.lock.acquire()
        timeAcquired = time.clock()
        timePassedSinceLastAcquire = timeAcquired - self.lastTimeAcquired
        timeToWait = self.period - timePassedSinceLastAcquire
        if (timeToWait > 0.0):
            PeriodicLock.logger.info("PeriodicLock: waiting %f sec" % timeToWait)
            time.sleep(timeToWait)
            
        self.lastTimeAcquired = timeAcquired
        self.lock.release()
        
        