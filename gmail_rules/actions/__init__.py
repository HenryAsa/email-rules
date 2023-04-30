"""
Initialize actions module
"""

def set_module(module):
    """Private decorator for overriding __module__ on a function or class.

    Example usage::

        @set_module('gmail_rules')
        def example():
            pass

        assert example.__module__ == 'gmail_rules'
    """
    def decorator(func):
        if module is not None:
            func.__module__ = module
        return func
    return decorator

from .rule_collection import Rule_Collection
from .build_xmls import build_xml_text

__all__ = [
    "Rule_Collection",
]