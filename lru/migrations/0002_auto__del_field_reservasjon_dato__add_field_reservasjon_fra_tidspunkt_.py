# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Reservasjon.dato'
        db.delete_column(u'lru_reservasjon', 'dato')

        # Adding field 'Reservasjon.fra_tidspunkt'
        db.add_column(u'lru_reservasjon', 'fra_tidspunkt',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 21, 0, 0)),
                      keep_default=False)

        # Adding field 'Reservasjon.til_tidspunkt'
        db.add_column(u'lru_reservasjon', 'til_tidspunkt',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 21, 0, 0)),
                      keep_default=False)

        # Adding field 'Reservasjon.kommentar'
        db.add_column(u'lru_reservasjon', 'kommentar',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 10, 21, 0, 0), max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Reservasjon.dato'
        db.add_column(u'lru_reservasjon', 'dato',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 21, 0, 0)),
                      keep_default=False)

        # Deleting field 'Reservasjon.fra_tidspunkt'
        db.delete_column(u'lru_reservasjon', 'fra_tidspunkt')

        # Deleting field 'Reservasjon.til_tidspunkt'
        db.delete_column(u'lru_reservasjon', 'til_tidspunkt')

        # Deleting field 'Reservasjon.kommentar'
        db.delete_column(u'lru_reservasjon', 'kommentar')


    models = {
        u'lru.reservasjon': {
            'Meta': {'object_name': 'Reservasjon'},
            'fra_tidspunkt': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kommentar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'reservert_av': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'til_tidspunkt': ('django.db.models.fields.DateTimeField', [], {}),
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