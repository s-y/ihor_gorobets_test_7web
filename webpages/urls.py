#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('main.urls')),
                       )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
        + \
        static(settings.MEDIA_URL,
               document_root=settings.MEDIA_ROOT)
