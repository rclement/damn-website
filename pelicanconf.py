#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Romain Clement'
SITENAME = 'digital audio for music nerds'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']

ARTICLE_PATHS = ['articles']
# ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Blogroll
LINKS = (
         ('Pelican', 'http://getpelican.com/'),
        )

# Social widget
SOCIAL = (
          ('github', 'https://github.com/rclement'),
          ('soundcloud', 'https://soundcloud.com/rclement'),
          ('linkedin', 'https://www.linkedin.com/in/romainclement'),
          ('viadeo', 'https://www.viadeo.com/fr/profile/romain.clement8'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
