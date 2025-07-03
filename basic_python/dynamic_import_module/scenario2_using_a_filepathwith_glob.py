from filecmp import cmpfiles
import imp
import importlib,sys
import pathlib

"""
gives all modules matching name pattern "other*.py
"""

other_libs = set(_.stem for _ in pathlib.Path.glob(pathlib.Path("."),"other*.py" ))


def loader(modulename) ->str:
   return importlib.import_module(modulename)

def main():
    lib_choice="other1"
    try:
         cmdline=sys.argv[1]
         if cmdline in other_libs:
            lib_choice=cmdline
    except IndexError:
        pass

    other = loader(lib_choice)
    x:str =other.x
    print(x)
    print(sys.argv[1])


if __name__=="__main__":
    main()