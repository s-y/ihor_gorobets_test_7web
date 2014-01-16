#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Note(models.Model):
    name = models.CharField(_('Name'), max_length=80, unique=True)
    text = models.TextField(_('Text'))
    done = models.BooleanField(_('Done'), default=False)
    image = models.ImageField(_('Image'), upload_to='notes_image', blank=True, null=True)

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

    def clean(self):
        if len(self.text) < 10:
            raise ValidationError(
                _('Text field must be at list 10 chars long'))

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(_('Name'), max_length=80, unique=True)
    notes = models.ManyToManyField(Note, verbose_name=_('Notes'), blank=True)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __unicode__(self):
        return self.name
