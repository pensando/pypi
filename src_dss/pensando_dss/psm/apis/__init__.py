import importlib
import os

from os import listdir
from os.path import isfile, join

ownpath = __file__.replace("__init__.py", "")

__all__ = [ name for name in os.listdir(ownpath) if (os.path.isdir(os.path.join(ownpath, name)) and not name.startswith("_")) ]

for i in __all__:
    module = importlib.import_module('.'+i, "pensando_dss.psm.apis")
    globals().update(
        {n: getattr(module, n) for n in module.__all__} if hasattr(module, '__all__') 
        else 
        {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')
    })
