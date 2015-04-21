#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Romain Clement'
SITENAME = 'digital audio for music nerds'
SITESUBTITLE = ''
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

LOAD_CONTENT_CACHE = False

THEME = 'themes/notmyidea-custom'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']

ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

TWITTER_USERNAME = 'romain_clement'

# Blogroll
# LINKS = (
#          ('Pelican', 'http://getpelican.com/'),
#         )

# Social widget
SOCIAL = (
          ('github', 'https://github.com/rclement'),
          ('soundcloud', 'https://soundcloud.com/rclement'),
          ('linkedin', 'https://www.linkedin.com/in/romainclement'),
          ('viadeo', 'https://www.viadeo.com/fr/profile/romain.clement8'),
          ('twitter', 'https://twitter.com/romain_clement'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
