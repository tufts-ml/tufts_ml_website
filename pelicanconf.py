#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Mike Hughes'
SITENAME = u'Machine Learning Research @ Tufts CS'
SITESUBTITLE = 'Models, Algorithms, and Applications'
DESCRIPTION = 'TODO'

if 'SITEURL' in os.environ:
    SITEURL = os.environ['SITEURL']
else:
    SITEURL = ''

OUTPUT_PATH = 'output/'
PATH = 'content/'

RELATIVE_URLS = True

THEME = 'themes/customized-pelican-alchemy/'

SITEIMAGE = '/images/tufts_ml_logo.png'

## LINKS ON MAIN NAVIGATION BAR
LINKS = [
    ('News', 'index.html'),
    ('People', 'people.html'),
    ('Events', 'events.html'),
    ('Courses', 'courses.html'),
]

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}


TIMEZONE = 'US/Eastern'
DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Theme-specific settings
DISPLAY_ARCHIVES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

ICONS = ()
SOCIAL = ()
HIDE_AUTHORS = True

