#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

from webpages.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
