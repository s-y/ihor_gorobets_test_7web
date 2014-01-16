# -*- coding: utf-8 -*-
from django.db import models
from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Note'
        db.create_table(u'main_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=80)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('done', self.gf('django.db.models.fields.BooleanField')
             (default=False)),
        ))
        db.send_create_signal(u'main', ['Note'])

    def backwards(self, orm):
        # Deleting model 'Note'
        db.delete_table(u'main_note')

    models = {
        u'main.note': {
            'Meta': {'object_name': 'Note'},
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['main']
