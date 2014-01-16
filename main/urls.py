#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from django.conf.urls import include, patterns, url

from .views import *

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'webpages.views.home', name='home'),
                       url(r'^note/add$', CreateNoteView.as_view(),
                           name='note_add'),
                       url(r'^$', ListNoteView.as_view(), name='notes'),
                       #url(r'^widget/', widget_view, name='widget'),
                       # url(r'^blog/', include('blog.urls')),

                       )
