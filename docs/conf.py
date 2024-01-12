
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Bay Crawler'
version = ''
release = ''

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
html_theme = 'alabaster'
html_static_path = ['_static']
