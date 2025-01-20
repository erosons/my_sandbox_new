import importlib

"""
gives you the flexibilty to dynamic import module with a lot complexity and not necessry 
import everything within the module, Gives you the flexibility selectively interact with a module.
"""

other=importlib.import_module("other1")

print(other.x)