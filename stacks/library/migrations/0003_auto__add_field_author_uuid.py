# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'library_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'library.book'], null=False)),
            ('author', models.ForeignKey(orm[u'library.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding field 'Author.uuid'
        db.add_column(u'library_author', 'uuid',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=36, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'library_book_authors'))

        # Deleting field 'Author.uuid'
        db.delete_column(u'library_author', 'uuid')


    models = {
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '36', 'db_index': 'True'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
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