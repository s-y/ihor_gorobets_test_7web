#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from django.template import Context, Template
from django.test import TestCase

from .models import *


class NotesViewsTestCase(TestCase):
    fixtures = ['initial_data.json']

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('Notes' in resp.content)

    def test_tag(self):
        Note.objects.create(**{'name': 'Test', 'text': 'Test text'})
        self.assert_(
            len(Template("""{% load custom_tag %}{% show_note "1" %}""").render(Context({}))) > 0, True)

    def test_post_notes(self):
        resp = self.client.post(
            '/note/add', {'name': 'Test', 'text': 'Test text'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Note.objects.get(name='Test').exists(), True)
        self.assertGreaterEqual(Note.objects.count(), 1)
