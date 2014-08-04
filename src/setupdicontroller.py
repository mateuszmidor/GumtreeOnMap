"""
This module must be imported before all others;
it is responsible for configuring the dependency injection controller
so that all the classes using injected dependencies are setup correctly
before they are first time used.
The configuration can be later reimplemented using some sort of config file
"""

from injectdependency import InjectDependency
from utf8printer import Utf8Printer

InjectDependency.registerDependency('printer', Utf8Printer)