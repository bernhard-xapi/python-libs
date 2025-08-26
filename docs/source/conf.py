# Configuration file for the Sphinx documentation builder.
# -- Path setup -------------------------------------------------------------
# Add project root to sys.path for autodoc to find xcp modules
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
# Add stubs directory to sys.path for stub modules (branding.py used )
sys.path.insert(0, os.path.abspath('../../stubs'))
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'python-libs'
copyright = '2025, Citrix Inc.'
author = 'Citrix Inc.'
from datetime import datetime
release = datetime.now().strftime('%Y.%m.%d-%H%M')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
