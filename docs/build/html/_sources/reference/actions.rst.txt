{{ header }}

.. _api.actions:

=====================
`Email-Rules` Actions
=====================

*******
Objects
*******

.. currentmodule:: gmail_rules

For some data types, pandas extends NumPy's type system. String aliases for these types
can be found at :ref:`basics.dtypes`.

=================== ==========================
Kind of Data        Data Type
=================== ==========================
Collection of Rules :class:`Rule_Collection`
=================== ==========================

Rule_Collection
---------------

.. warning::

    This feature is experimental, and the API can change in a future release without warning.

The :class:`actions.Rule_Collection` contains a collection of :class:`rules.rule.Rule`


.. autosummary::
   :toctree: api/

   actions.rule_collection
