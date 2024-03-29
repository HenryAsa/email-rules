"""
Initialize rules module
"""


from .rule import Rule
from .copy_to import Copy_To
from .move_to import Move_To


__all__ = [
    "Rule",
    "Copy_To",
    "Move_To",
]

# from . import rule_classes

# from os.path import dirname, basename, isfile, join
# import glob
# modules = glob.glob(join(dirname(__file__), "*.py"))

# for f in modules:
#     if isfile(f) and not f.endswith('__init__.py'):
#         exec(f"from .{basename(f)[:-3]} import *")
