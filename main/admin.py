#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from django.contrib import admin

from .forms import *
from .models import *


class NoteAdmin(admin.ModelAdmin):
    form = AddNoteForm

admin.site.register(Note, NoteAdmin)
