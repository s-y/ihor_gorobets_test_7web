#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from .models import *


def note_processor(request):
    return {'note_amaunt': Note.objects.count()}
