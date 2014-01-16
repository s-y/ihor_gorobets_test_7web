#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



class UpperCaseField(forms.CharField):

    def clean(self, value):
        value = ''.join(char for char in value if char.isupper())
        if value == '':
            raise ValidationError(
                _('Field with value must have at least 1 upper char'))
        else:
            return value
