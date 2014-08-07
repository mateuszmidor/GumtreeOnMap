'''
Created on 05-08-2014

@author: mateusz
@summary: This module configures dependency injection controller to be used in unit tests
@attention: This module should be included in every unit test to ensuce DI works properly
'''
from injectdependency import InjectDependency

class EmptyStub():
    pass

# Register all dependencies that will be needed in tests
# For now set them to some dummy value, they will be changed in tests
InjectDependency.registerDependency('logger', EmptyStub)
InjectDependency.registerDependency('urlfetcher', EmptyStub)
InjectDependency.registerDependency('geocoder', EmptyStub)
InjectDependency.registerDependency('printer', EmptyStub)
InjectDependency.registerDependency('addressresolver', EmptyStub)