# -*- coding: utf-8 -*-
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
from sphinx.locale import admonitionlabels

# -- Project information -----------------------------------------------------

project = "JPSC codebook"
copyright = "2019, KEIO PDRC"
author = "JPSC"

# The short X.Y version
version = "0.1"
# The full version, including alpha/beta/rc tags
release = "1"

html_last_updated_fmt = "%b %d, %Y"

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = [
#    'sphinx.ext.todo',
#    'sphinx.ext.githubpages',]
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.graphviz",
    "sphinxcontrib.inkscapeconverter",
]
blockdiag_html_image_format = "SVG"
inkscape_converter_bin = "/usr/bin/inkscape"
# Fontpath for blockdiag (truetype font)

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "ja"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

html_logo = "_static/jpsclogo.png"
html_favicon = "_static/jpsc.ico"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = ["sphinx_rtd_theme.get_html_theme_path()"]


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "titles_only": True,
    "navigation_depth": 3,
    "sticky_navigation": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#


# html_sidebars = {}
# 国際化
locale_dirs = ["locale/"]  # path is example but recommended.
gettext_compact = False  # optional.

# 先頭に文字
rst_prolog = u"""
.. include:: /definition.txt
"""
# CSSの追加
def setup(app):
    app.add_stylesheet("my.css")


admonitionlabels["note"] = u"notice"
admonitionlabels["warning"] = u"warning"
admonitionlabels["hint"] = u""
