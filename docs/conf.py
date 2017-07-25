#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# AnyPyTools documentation build configuration file, created by
# sphinx-quickstart on Fri Jul 21 15:33:03 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from anypytools import __version__ as ANYPYTOOLS_VERSION
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

import cloud_sptheme


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'nbsphinx',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_console_highlighting',
    'cloud_sptheme.ext.autodoc_sections',
    'cloud_sptheme.ext.index_styling',
    'cloud_sptheme.ext.relbar_toc',
    'cloud_sptheme.ext.escaped_samp_literals',
    'cloud_sptheme.ext.issue_tracker',
    'cloud_sptheme.ext.table_styling',
    ]

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_parsers = {
   '.md': CommonMarkParser,
}



# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'AnyPyTools'
copyright = '2017, Morten Enemark Lund'
author = 'Morten Enemark Lund'

github_doc_root = 'https://github.com/anybody-research-group/anypytools/tree/master/docs/'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ANYPYTOOLS_VERSION.rsplit('.',1)[0]
# The full version, including alpha/beta/rc tags.
release = ANYPYTOOLS_VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'slides', 'Tutorial/00_*.ipynb' ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "cloud"

html_theme_path = [cloud_sptheme.get_theme_dir()]


#html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'roottarget': 'index' ,
    'max_width': '1250px',
    'minimal_width': '700px',
    'borderless_decor':True,
    'sidebarwidth':"3in",
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/anypytools_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/anypytools.ico'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'AnyPyToolsdoc'


html_logo = '_static/anypytools_logo.png'


nbsphinx_execute = 'never'



# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'AnyPyTools.tex', 'AnyPyTools Documentation',
     'Morten Enemark Lund', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'anypytools', 'AnyPyTools Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'AnyPyTools', 'AnyPyTools Documentation',
     author, 'AnyPyTools', 'One line description of project.',
     'Miscellaneous'),
]


#Autodocumentation Flags
autodoc_member_order = "groupwise"
autoclass_content = "both"
autosummary_generate = []

# Prevent numpy from making silly tables
numpydoc_show_class_members = False

def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
