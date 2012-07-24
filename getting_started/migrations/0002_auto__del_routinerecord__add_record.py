# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RoutineRecord'
        db.delete_table('getting_started_routinerecord')

        # Adding model 'Record'
        db.create_table('getting_started_record', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('weight_int', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('weight_dec', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('morning_drug_size', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('morning_drug_amount_int', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('morning_drug_amount_dec', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('afternoon_drug_size', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('afternoon_drug_amount_int', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('afternoon_drug_amount_dec', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('evening_drug_size', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('evening_drug_amount_int', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('evening_drug_amount_dec', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_up_first', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_down_first', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_up_second', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_down_second', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_up_third', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_down_third', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('heartrate_first', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('heartrate_second', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('heartrate_third', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('optional_first', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('optional_second', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('optional_third', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('voicemail', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('reply_message', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('reply_nurse', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('reply_needed', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('getting_started', ['Record'])


    def backwards(self, orm):
        # Adding model 'RoutineRecord'
        db.create_table('getting_started_routinerecord', (
            ('optional_third', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('afternoon_drug_amount_int', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('heartrate_second', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('evening_drug_amount_int', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('reply_nurse', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('morning_drug_amount_dec', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('heartrate_third', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('weight_int', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_up_first', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_down_first', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('morning_drug_size', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('afternoon_drug_size', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('evening_drug_amount_dec', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('heartrate_first', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('weight_dec', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('evening_drug_size', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_up_second', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('reply_needed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('optional_first', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_up_third', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_down_third', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('voicemail', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('optional_second', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('reply_message', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('afternoon_drug_amount_dec', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('morning_drug_amount_int', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pressure_down_second', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('getting_started', ['RoutineRecord'])

        # Deleting model 'Record'
        db.delete_table('getting_started_record')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'getting_started.record': {
            'Meta': {'object_name': 'Record'},
            'afternoon_drug_amount_dec': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'afternoon_drug_amount_int': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'afternoon_drug_size': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'evening_drug_amount_dec': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'evening_drug_amount_int': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'evening_drug_size': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'heartrate_first': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'heartrate_second': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'heartrate_third': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning_drug_amount_dec': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'morning_drug_amount_int': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'morning_drug_size': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'optional_first': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'optional_second': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'optional_third': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'pressure_down_first': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pressure_down_second': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pressure_down_third': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pressure_up_first': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pressure_up_second': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pressure_up_third': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'reply_message': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'reply_needed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'reply_nurse': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'voicemail': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'weight_dec': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'weight_int': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['getting_started']