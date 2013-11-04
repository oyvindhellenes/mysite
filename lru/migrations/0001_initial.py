# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Utstyr'
        db.create_table(u'lru_utstyr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('utstyrstype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('beskrivelse', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('lokasjon', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'lru', ['Utstyr'])

        # Adding model 'Reservasjon'
        db.create_table(u'lru_reservasjon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('utstyr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lru.Utstyr'])),
            ('dato', self.gf('django.db.models.fields.DateTimeField')()),
            ('reservert_av', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'lru', ['Reservasjon'])


    def backwards(self, orm):
        # Deleting model 'Utstyr'
        db.delete_table(u'lru_utstyr')

        # Deleting model 'Reservasjon'
        db.delete_table(u'lru_reservasjon')


    models = {
        u'lru.reservasjon': {
            'Meta': {'object_name': 'Reservasjon'},
            'dato': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reservert_av': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'utstyr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lru.Utstyr']"})
        },
        u'lru.utstyr': {
            'Meta': {'object_name': 'Utstyr'},
            'beskrivelse': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lokasjon': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'utstyrstype': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lru']