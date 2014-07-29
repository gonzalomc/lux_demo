# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OtImage'
        db.create_table('ot_images', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ot', self.gf('django.db.models.fields.related.ForeignKey')(related_name='image', to=orm['webapp.Ot'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('webapp', ['OtImage'])

        # Adding model 'Technical'
        db.create_table('technical', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('rut', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal('webapp', ['Technical'])

        # Adding model 'Field'
        db.create_table('fields', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webapp.Section'])),
        ))
        db.send_create_signal('webapp', ['Field'])

        # Adding model 'Section'
        db.create_table('sections', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('webapp', ['Section'])

        # Adding model 'Ot'
        db.create_table('ot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='1', max_length=50)),
            ('technical', self.gf('django.db.models.fields.related.ForeignKey')(related_name='technical', to=orm['webapp.Technical'])),
        ))
        db.send_create_signal('webapp', ['Ot'])


    def backwards(self, orm):
        # Deleting model 'OtImage'
        db.delete_table('ot_images')

        # Deleting model 'Technical'
        db.delete_table('technical')

        # Deleting model 'Field'
        db.delete_table('fields')

        # Deleting model 'Section'
        db.delete_table('sections')

        # Deleting model 'Ot'
        db.delete_table('ot')


    models = {
        'webapp.field': {
            'Meta': {'object_name': 'Field', 'db_table': "'fields'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['webapp.Section']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'webapp.ot': {
            'Meta': {'object_name': 'Ot', 'db_table': "'ot'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50'}),
            'technical': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'technical'", 'to': "orm['webapp.Technical']"})
        },
        'webapp.otimage': {
            'Meta': {'object_name': 'OtImage', 'db_table': "'ot_images'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image'", 'to': "orm['webapp.Ot']"})
        },
        'webapp.section': {
            'Meta': {'object_name': 'Section', 'db_table': "'sections'"},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'webapp.technical': {
            'Meta': {'object_name': 'Technical', 'db_table': "'technical'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rut': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['webapp']