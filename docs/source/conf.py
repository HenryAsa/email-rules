# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'email-rules'
copyright = '2023, Henry Asa'
author = 'Henry Asa'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = '.rst'

extensions = [
    'sphinx.ext.autodoc',
    # 'numpydoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    # 'sphinx_design'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]

# -----------------------------------------------------------------------------
# Intersphinx configuration
# -----------------------------------------------------------------------------
intersphinx_mapping = {
    'neps': ('https://numpy.org/neps', None),
    'python': ('https://docs.python.org/3', None),
    'scipy': ('https://docs.scipy.org/doc/scipy', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    'imageio': ('https://imageio.readthedocs.io/en/stable', None),
    'skimage': ('https://scikit-image.org/docs/stable', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'scipy-lecture-notes': ('https://scipy-lectures.org', None),
    'pytest': ('https://docs.pytest.org/en/stable', None),
    'numpy-tutorials': ('https://numpy.org/numpy-tutorials', None),
    'numpydoc': ('https://numpydoc.readthedocs.io/en/latest', None),
    'dlpack': ('https://dmlc.github.io/dlpack/latest', None)
}

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------
autosummary_generate = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'pydata_sphinx_theme'
# html_static_path = ['_static']

"""
# Configure the Sphinx Autodoc extension (sphinx.ext.autodoc) so the generated
# API reference shows all members (methods, etc.) rather than just some.
autodoc_default_flags = [
    'members',
    'private-members',
    'special-members',
    'undoc-members',
    'inherited-members',
    'show-inheritance',
]
"""

autodoc_default_flags = [
    'members',
    'private-members',
    'special-members',
    'undoc-members',
    'inherited-members',
    'show-inheritance',
]

html_theme_options = {
    "github_url": "https://github.com/HenryAsa/email-rules",
}
