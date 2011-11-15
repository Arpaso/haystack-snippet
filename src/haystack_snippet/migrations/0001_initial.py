# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SearchLogger'
        db.create_table('haystack_snippet_searchlogger', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('counter', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('last_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('haystack_snippet', ['SearchLogger'])


    def backwards(self, orm):
        
        # Deleting model 'SearchLogger'
        db.delete_table('haystack_snippet_searchlogger')


    models = {
        'haystack_snippet.searchlogger': {
            'Meta': {'ordering': "('-counter',)", 'object_name': 'SearchLogger'},
            'counter': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['haystack_snippet']
