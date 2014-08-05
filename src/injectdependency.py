'''
Created on 04-08-2014

@author: mateusz
'''

class Inject():
    """
    Dependency Injection marker.
    Assign to fields that are supposed to be subject of dependency injection, eg.
    
    @InjectDependency('dependency') 
    class Example():
        dependency = Inject
    """
    def str(self):
        return "[This field should be substituted with actual value by @InjectDependency decorator]"

class DependencyInjectionException(Exception):
    pass

class DependencyProxy():
    """
    We actually inject proxy to given object, not the object itself.
    This way we can easily exchange one dependency for another
    even after all dependencies have already been injected
    """
    
    # proxy target
    target = None
    
    def __init__(self, target):
        self.setProxyTarget(target)
        
    def __getattr__(self, name):
        return getattr(self.target, name)
        
    # should there be __setattr__ as well???
    
    def setProxyTarget(self, target):
        self.target = target
        
class InjectDependency():
    """"Dependency injection decorator for classes"""
    
    # dictionary with "dependencyName : value" pairs 
    dependencies = {}
    
    def __init__(self, *dependenciesToInject):
        """takes list of dependencies names to be injected into the class"""
        self.dependenciesToInject = dependenciesToInject
    
    def __call__(self, targetClass):
        """takes target class to inject dependencies into"""
        
        for name in self.dependenciesToInject: 
            InjectDependency.throwIfDependencyNotRegistered(name)
            InjectDependency.throwIfNoSuchField(name, targetClass)
            InjectDependency.throwIfFieldNotDesignatedForInjection(name, targetClass)
            setattr(targetClass, name, InjectDependency.dependencies[name])
            
        # return class with injected dependencies
        return targetClass

    @staticmethod
    def registerDependency(name, value):
        InjectDependency.throwIfDependencyAlreadyRegistered(name)
        InjectDependency.dependencies[name] = DependencyProxy(value)
 
    @staticmethod 
    def changeDependency(name, value):
        InjectDependency.throwIfDependencyNotRegistered(name)
        InjectDependency.dependencies[name].setProxyTarget(value)
            
    @staticmethod
    def throwIfDependencyNotRegistered(name):
        ERROR_STR = 'Dependency not registered "%s". Use "registerDependency"'
        if (name not in InjectDependency.dependencies):
            raise DependencyInjectionException(ERROR_STR % name)
  
    @staticmethod
    def throwIfDependencyAlreadyRegistered(name):
        ERROR_STR = 'Dependency already registered "%s". Use "changeDependency"'
        if (name in InjectDependency.dependencies):
            raise DependencyInjectionException(ERROR_STR % name)
          
    @staticmethod
    def throwIfNoSuchField(name, targetClass):
        ERROR_STR = 'Cant inject dependency. No field "%s" in class "%s"'
        if (name not in targetClass.__dict__):
            raise DependencyInjectionException(ERROR_STR % (name, targetClass.__name__))
        
    @staticmethod
    def throwIfFieldNotDesignatedForInjection(name, targetClass):
        ERROR_STR = 'Field "%s.%s" not designated for injection. Should be initially set to "Inject" instead of "%s"'
        if (targetClass.__dict__[name] != Inject):
            raise DependencyInjectionException(ERROR_STR % ( targetClass.__name__, name, targetClass.__dict__[name]))