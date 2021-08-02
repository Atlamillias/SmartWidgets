
import warnings
import _writelib

AUTO_UPDATE = True

def update_library():
    try:
        _writelib.main()
    except PermissionError as e:
        warnings.warn(f"A PermissionError was raised trying to update the library - {str(e)}.")

if AUTO_UPDATE and __name__ != "__main__":
    update_library()



import lib
from lib import *


__all__ = [*lib.__all__, "item", "widget", "update_library"]

