# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from psm.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

import importlib
import os

from os import listdir
from os.path import isfile, join

ownpath = __file__.replace("__init__.py", "")

__all__ = [ name for name in os.listdir(ownpath) if (os.path.isdir(os.path.join(ownpath, name)) and not name.startswith("_")) ]

for i in __all__:
    module = importlib.import_module('.'+i, "pensando_dss.psm.models")
    globals().update(
        {n: getattr(module, n) for n in module.__all__} if hasattr(module, '__all__') 
        else 
        {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')
    })
