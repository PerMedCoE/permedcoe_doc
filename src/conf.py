# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PerMedCoE Base Package'
copyright = '2021, PerMedCoE Project'
author = 'PerMedCoE Project'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_rtd_theme",
              'sphinx.ext.duration',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.imgmath',
              'sphinx.ext.ifconfig',
              'sphinx.ext.imgconverter',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.mathjax',
              'myst_parser',
              'sphinxcontrib.contentui',
              'sphinx_copybutton',
              'sphinxcontrib.spelling',
              'sphinx_panels'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['../_build', '../Thumbs.db', '../.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"  # 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    '_templates/custom.css',
]

html_theme_options = {
    'logo_only': True,
    # 'display_version': True,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    'navigation_depth': 5,
    # 'includehidden': True,
    # 'titles_only': False
}

# Specific configuration
numfig_format = {'figure':'Figure %s',
                 'table':'Table %s',
                 'code-block':'Code %s',
                 'section':'Section %s'}
html_logo = "../_static/logo_1.png"
html_show_sourcelink = False
html_favicon = "../_static/logo_1.ico"

# True to prefix each section label with the name of the document it is in,
# followed by a colon.
autosectionlabel_prefix_document = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default' # 'sphinx'

html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"]
panels_add_fontawesome_latex = True
