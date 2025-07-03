import importlib.util

"""
gives you the flexibilty to dynamic import module with a lot complexity and not necessry 
import everything within the module, Gives you the flexibility selectively interact with a module.
"""

spec=importlib.util.spec_from_file_location("other1","Engineering/Personal_Implemenation/tutorial/dynamic_import_module/other1.py")
#spec: Module spec location is return file path
#namespace containing the related module is ued

other=spec.loader.load_module()
print(other.x)