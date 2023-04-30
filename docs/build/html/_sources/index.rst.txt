.. email-rules documentation master file, created by
   sphinx-quickstart on Sun Apr  9 01:06:54 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#############################
Documentation for Email-Rules
#############################

**Date**: |today| **Version**: |version|

:mod:`email-rules` is an open source package designed to create email rules
for email clients (such as Gmail) to organize and streamline your inbox. 

.. grid:: 1 2 2 2
   :gutter: 4
   :padding: 2 2 0 0
   :class-container: sd-text-center

   .. grid-item-card:: Getting Started
      :img-top: _static/index_getting_started.svg
      :class-card: intro-card
      :shadow: md

      New to :mod:`email-rules`?  Check out the Getting Started guides.  They
      contain information about how to use this package, its purpose, and a
      few tutorials.

      +++

      .. button-ref:: getting_started
         :ref-type: ref
         :click-parent:
         :color: secondary
         :expand:

         Getting Started Guides

   .. grid-item-card::  User Guide
      :img-top: _static/index_user_guide.svg
      :class-card: intro-card
      :shadow: md

      The user guide provides more in-depth information on the key concepts of
      :mod:`email-rules` and explanations of some of its features.

      +++

      .. button-ref:: user_guide
         :ref-type: ref
         :click-parent:
         :color: secondary
         :expand:

         User Guide

   .. grid-item-card::  API Reference
      :img-top: _static/index_api.svg
      :class-card: intro-card
      :shadow: md

      This reference guide for :mod:`email-rules` contains detailed descriptions of how the
      actual code works, how it should be used, and references.  It describes how the methods
      work, what types of parameters they are intended to work with, and additional info.

      +++

      .. button-ref:: api
         :ref-type: ref
         :click-parent:
         :color: secondary
         :expand:

         API Reference Guide

   .. grid-item-card::  Developer Guide
      :img-top: _static/index_contribute.svg
      :class-card: intro-card
      :shadow: md

      This section outlines how you can contribute to the :mod:`email-rules`
      package!  Review the Contributing Guidelines, and help us improve
      the module; we're always looking for improvements and new features!

      +++

      .. button-ref:: development
         :ref-type: ref
         :click-parent:
         :color: secondary
         :expand:

         Development Guide


{% endif %}
{% if single_doc and single_doc.endswith('.rst') -%}
.. toctree::
   :maxdepth: 3
   :titlesonly:

   {{ single_doc[:-4] }}
{% elif single_doc and single_doc.count('.') <= 1 %}
.. autosummary::
   :toctree: reference/api/

   {{ single_doc }}
{% elif single_doc %}
.. autosummary::
   :toctree: reference/api/
   :template: autosummary/accessor_method.rst

   {{ single_doc }}
{% else -%}
.. toctree::
   :maxdepth: 3
   :hidden:
   :titlesonly:
{% endif %}
{% if not single_doc %}
   getting_started/index
   user_guide/index
   {% endif -%}
   {% if include_api -%}
   reference/index
   {% endif -%}
   {% if not single_doc -%}
   development/index
   whatsnew/index
{% endif %}

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`