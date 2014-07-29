# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.name'
        db.alter_column('product', 'name', self.gf('django.db.models.fields.CharField')(default='default_name', max_length=70))

    def backwards(self, orm):

        # Changing field 'Product.name'
        db.alter_column('product', 'name', self.gf('django.db.models.fields.CharField')(max_length=70, null=True))

    models = {
        'webapp.client': {
            'Meta': {'object_name': 'Client', 'db_table': "'client'"},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'webapp.field': {
            'Meta': {'object_name': 'Field', 'db_table': "'fields'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'field'", 'to': "orm['webapp.Section']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '200'})
        },
        'webapp.ot': {
            'Meta': {'object_name': 'Ot', 'db_table': "'ot'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['webapp.Product']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '50'}),
            'technical': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'technical'", 'null': 'True', 'to': "orm['webapp.Technical']"})
        },
        'webapp.otimage': {
            'Meta': {'object_name': 'OtImage', 'db_table': "'ot_images'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image'", 'to': "orm['webapp.Ot']"})
        },
        'webapp.product': {
            'Meta': {'object_name': 'Product', 'db_table': "'product'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rut': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['webapp']