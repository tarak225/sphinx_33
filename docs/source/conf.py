#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its containing dir.
#

import sys
import os
# on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# if not on_rtd:  # only import and set the theme if we're building docs locally
#     import sphinx_rtd_theme
#     html_theme = 'sphinx_rtd_theme'
#     html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# If the directory is relative to the documentation root, use os.path.abspath to make it absolute, like shown here.
# directory relative to this conf file
CURDIR = os.path.abspath(os.path.dirname(__file__))

# If extensions (or modules to document with auto-doc) are in another directory, add these directories to sys.path here.
# add custom extensions directory to python path
#sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '_extensions'))

# -- General configuration ---------------------------------------------------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx',
              'sphinxcontrib.exceltable',
             # 'sphinxcontrib.napoleon',
              'sphinxcontrib.bibtex',
              'sphinxcontrib.httpdomain',
             ]

mathjax_path = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# -- bibtex configuration settings ---------------------------------------------------------

bibtex_bibfiles = ['13_dir/$_14-reference-1-book-food-method.bib',
                            '13_dir/$_14-reference-2-article-food-method.bib',
                            '13_dir/$_14-reference-3-book-food-ref.bib',
                            '13_dir/$_14-reference-4-article-food-ref.bib',
                            '13_dir/$_14-reference-5-misc-ontology.bib',
                            '13_dir/$_14-reference-6-misc-data.bib',
                            '13_dir/$_14-reference-7-misc-web.bib',
                            '13_dir/$_14-reference-8-article-technology.bib',
                           ]


# -- Intersphinx ---------------------------------------------------------------

intersphinx_cache_limit = 10     # days to keep the cached inventories
intersphinx_mapping = {
       # 'sphinx':('http://sphinx.pocoo.org',None),
        'python':('http://docs.python.org/3.2',None),
    'matplotlib':('http://matplotlib.sourceforge.net',None),
         'numpy':('http://docs.scipy.org/doc/numpy',None),
}

# -- Options for Napoleon Extension --------------------------------------------

# Parse Google style docstrings.
# See http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
napoleon_google_docstring = True

# Parse NumPy style docstrings.
# See https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
napoleon_numpy_docstring = False

# Should special members (like __membername__) and private members (like _membername) members be included
# in the documentation if they have docstrings.
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# If True, docstring sections will use the ".. admonition::" directive.
# If False, docstring sections will use the ".. rubric::" directive.
# One may look better than the other depending on what HTML theme is used.
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False

# If True, use Sphinx :ivar: directive for instance variables:
#     :ivar attr1: Description of attr1.
#     :type attr1: type
# If False, use Sphinx .. attribute:: directive for instance variables:
#     .. attribute:: attr1
#
#        *type*
#
#        Description of attr1.
napoleon_use_ivar = False

# If True, use Sphinx :param: directive for function parameters:
#     :param arg1: Description of arg1.
#     :type arg1: type
# If False, output function parameters using the :parameters: field:
#     :parameters: **arg1** (*type*) -- Description of arg1.
napoleon_use_param = True

# If True, use Sphinx :rtype: directive for the return type:
#     :returns: Description of return value.
#     :rtype: type
# If False, output the return type inline with the return description:
#     :returns: *type* -- Description of return value.
napoleon_use_rtype = True

# -- Autodoc configuration -----------------------------------------------------------------

autoclass_content = 'class'

autodoc_member_order = 'bysource'

autodoc_default_flags = ['members']

# -- More general configuration ------------------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# Project information. Label goes into left nav title block
project = 'USDA Nutrition Database'
#copyright = '2014, Ontomatica'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the built documents.
# The short X.Y version.
#version = '1.1'
# The full version, including alpha/beta/rc tags.
#release = 'a'

# Turns on numbered figures for HTML output
number_figures = True

# The language for content auto-generated by Sphinx. Refer to documentation for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
#language = None

# There are two options for replacing |today|: either, you set today to some non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%d %B %Y'

# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
exclude_patterns = [
                    '_build',
                    'epilog.rst',
                    '_sphinx_lib',
                   ]

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be pre-pended to all description unit titles (such as .. function::).
#add_module_names = True

# If true, section-author and module-author directives will be shown in the output. They are ignored by default.
#show_authors = False

# A string of reStructuredText that will be included at the end of every source file that is read.
# decode fails: rst_epilog = open(os.path.join(CURDIR, 'epilog.rst'),'r').read().decode('utf-8')
# rst_epilog = open(os.path.join(CURDIR, 'epilog.rst'),'r').read()

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ---------------------------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for a list of built-in themes.
#html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme further.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents. Appears in browser tab.
# If None, it defaults to "<project> v<release> documentation".
html_title = ""

# A shorter title for the navigation bar. Default is the same as html_title.
#html_short_title = "USDA Database"

# The name of an image file (relative to this directory) to place at the top of the sidebar.
#html_logo = 'ars-logo.png'

# The name of an image file (within the static path) to use as favicon of the docs.
# This file should be a Windows icon file (.ico) being 16x16 or 32x32 pixels large.
#html_favicon = "USDA_ARS.png"

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory.
# They are copied after the built-in static files, so a file named "default.css" will overwrite the built-in "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or .htaccess) here, relative to this directory.
# These files are copied directly to the root of the documentation.
#html_extra_path = ['_images']

# If not '', a 'Last updated on:' time-stamp is inserted at every page bottom, using the given strftime format.
#html_last_updated_fmt = '%d %b %Y'

# If true, SmartyPants will be used to convert quotes and dashes to typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright Ontomatica" is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will contain a <link> tag referring to it.
# The value of this option must be the base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = '.html'

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that implements a search results scorer.
# If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'htmlhelpoutput'

# -- Options for LaTeX output ---------------------------------------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': '',

# Latex figure (float) alignment
'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
                  ('index', 'sample_doc.tex', 'sample\\_doc Documentation', 'hidepy', 'manual'),
                  ]

# The name of an image file (relative to this directory) to place at the top of the title page.
latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts, not chapters.
latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output -----------------------------------------------------------

# One entry per manual page.
# List of tuples (source start file, name, description, authors, manual section).
man_pages = [
            ('index', 'sample_doc', 'sample_doc Documentation', ['hidepy'], 1)
            ]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for Texinfo output ---------------------------------------------------------------

# Grouping the document tree into Texinfo files.
# List of tuples (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [
                    ('index', 'sample_doc', 'sample_doc Documentation', 'hidepy', 
                    'sample_doc', 'One line description of project.', 'Miscellaneous'),
                    ]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

