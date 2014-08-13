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

class NotRegistered():
    """
    Dependency Injection pending registration marker.
    If we need to _inject dependency that has not been registered yet,
    we _inject this class to mark that it needs registration prior to use
    """
    def str(self):
        return "[Dependency for this field should be registered by InjectDependency.registerDependency]"
    
class DependencyInjectionException(Exception):
    pass

class DependencyProxy():
    """
    We actually _inject proxy to given object, not the object itself.
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
    
    def __call__(self, targetObject):
        """takes target class to _inject dependencies into"""
        for name in self.dependenciesToInject: 
            InjectDependency._throwIfNoSuchField(name, targetObject)
            InjectDependency._throwIfFieldNotDesignatedForInjection(name, targetObject)
            InjectDependency._registerIfNotRegistered(name)
            InjectDependency._inject(name, targetObject)
            
        # return class with injected dependencies
        return targetObject

    @staticmethod
    def _registerIfNotRegistered(name):
        if (name not in InjectDependency.dependencies):
            InjectDependency.dependencies[name] = DependencyProxy(NotRegistered)      
             
    @staticmethod
    def _inject(dependencyName, targetObject):
        setattr(targetObject, dependencyName, InjectDependency.dependencies[dependencyName])
          
    @staticmethod
    def manualInject(fieldName, value, targetObject):
        """ this method is to avoid automatic DI machinery in tests; use it in tests"""
        InjectDependency._throwIfNoSuchField(fieldName, targetObject)
        setattr(targetObject, fieldName, value)
          
    @staticmethod
    def setDependency(name, value):
        InjectDependency._registerIfNotRegistered(name)
        InjectDependency.dependencies[name].setProxyTarget(value)
            
    @staticmethod
    def _throwIfNoSuchField(name, targetClass):
        ERROR_STR = 'Cant _inject dependency. No field "%s" in class "%s"'
        if (name not in targetClass.__dict__):
            raise DependencyInjectionException(ERROR_STR % (name, targetClass.__name__))
        
    @staticmethod
    def _throwIfFieldNotDesignatedForInjection(name, targetClass):
        ERROR_STR = 'Field "%s.%s" not designated for injection. Should be initially set to "Inject" instead of "%s"'
        if (targetClass.__dict__[name] != Inject): 
            raise DependencyInjectionException(ERROR_STR % ( targetClass.__name__, name, targetClass.__dict__[name]))