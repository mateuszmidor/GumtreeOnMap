'''
Created on 04-08-2014

@author: mateusz
'''

# injection target marker, eg.
# @InjectDependency('fieldToBeInjected') 
# class Injection():
#     fieldToBeInjected = Inject
Inject = "[inject instance for this field]"

class DependencyInjectionException(Exception):
    pass

class InjectDependency():
    """"dependency injection decorator for classes"""
    
    # dictionary with dependency_name : value pairs 
    dependencies = { }
    
    def __init__(self, *dependenciesToInject):
        """takes list of dependencies names to be injected into a class"""
        self.dependenciesToInject = dependenciesToInject
    
    def __call__(self, targetClass):
        """takes target class to inject dependencies into"""
        
        for name in self.dependenciesToInject: 
            self.throwIfDependencyNotRegistered(name)
            self.throwIfNoSuchField(name, targetClass)
            self.throwIfFieldNotDesignatedForInjection(name, targetClass)
            targetClass.__dict__[name] = InjectDependency.dependencies[name]
    
        # return class with injected dependencies
        return targetClass
    
    def throwIfDependencyNotRegistered(self, name):
        ERROR_STR = 'Cant inject not registered dependency "%s"'
        if (name not in InjectDependency.dependencies):
            raise DependencyInjectionException(ERROR_STR % name)
    
    def throwIfNoSuchField(self, name, targetClass):
        ERROR_STR = 'Cant inject dependency. No field "%s" in class "%s"'
        if (name not in targetClass.__dict__):
            raise DependencyInjectionException(ERROR_STR % (name, targetClass.__name__))
        
    def throwIfFieldNotDesignatedForInjection(self, name, targetClass):
        ERROR_STR = 'Field "%s.%s" not designated for injection. Should be initially set to "Inject" instead of "%s"'
        if (targetClass.__dict__[name] != Inject):
            raise DependencyInjectionException(ERROR_STR % ( targetClass.__name__, name, targetClass.__dict__[name]))
        
    @staticmethod
    def registerDependency(name, value):
        InjectDependency.dependencies[name] = value