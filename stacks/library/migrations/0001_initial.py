# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'library_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default=None, max_length=36, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('author_lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author_firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('publish_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('isbn10', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('isbn13', self.gf('django.db.models.fields.CharField')(max_length=13, null=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'library', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'library_book')


    models = {
        u'library.book': {
            'Meta': {'object_name': 'Book'},
            'author_firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'author_lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn10': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'isbn13': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '36', 'db_index': 'True'})
        }
    }

    complete_apps = ['library']