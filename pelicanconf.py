#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'solj'
SITENAME = u'Bcfg2'
SITEURL = 'http://bcfg2.org'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME="themes/bcfg2"

DISPLAY_PAGES_ON_MENU=False
MENUITEMS = [
    ('Download', '/download/'),
    ('Documentation', 'http://docs.bcfg2.org'),
    ('Install', 'http://docs.bcfg2.org/installation/index.html'),
    ('Contribute', '/contribute/')
]

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

GITHUB_URL = 'https://github.com/Bcfg2/bcfg2'

READERS = {'html': None}
STATIC_PATHS = ['downloads', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {
        'path': 'favicon.ico'}
}
