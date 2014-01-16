# -*- coding: utf-8 -*-
from django.db import models
from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Note.image'
        db.add_column(u'main_note', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(
                          max_length=100, null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Note.image'
        db.delete_column(u'main_note', 'image')

    models = {
        u'main.note': {
            'Meta': {'object_name': 'Note'},
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['main']
