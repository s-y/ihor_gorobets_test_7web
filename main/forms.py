#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from .fields import *
from .models import *


class AddNoteForm(forms.ModelForm):
    name = UpperCaseField()

    class Meta:
        model = Note
