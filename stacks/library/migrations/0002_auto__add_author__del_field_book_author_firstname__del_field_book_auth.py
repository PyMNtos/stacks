# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'library_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'library', ['Author'])

        # Deleting field 'Book.author_firstname'
        db.delete_column(u'library_book', 'author_firstname')

        # Deleting field 'Book.author_lastname'
        db.delete_column(u'library_book', 'author_lastname')


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'library_author')

        # Adding field 'Book.author_firstname'
        db.add_column(u'library_book', 'author_firstname',
                      self.gf('django.db.models.fields.CharField')(default='Empty', max_length=50),
                      keep_default=False)

        # Adding field 'Book.author_lastname'
        db.add_column(u'library_book', 'author_lastname',
                      self.gf('django.db.models.fields.CharField')(default='Empty', max_length=50),
                      keep_default=False)


    models = {
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book'},
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