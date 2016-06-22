#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Silviu Pitis'
SITENAME = 'R2RT'
SITEURL = 'http://localhost:8000'
THEME = "./theme"

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

#Random settings
GITHUB_URL = 'https://github.com/spitis'
TYPEKIT_URL = 'https://use.typekit.net/wat7zgx.js'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#PLUGINS
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']

STATIC_PATHS = ['static']


# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
