#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe

from ..models import *

register = template.Library()


@register.inclusion_tag('base/note_one.html')
def show_note(id):
    return {'object': Note.objects.get(pk=id)}
