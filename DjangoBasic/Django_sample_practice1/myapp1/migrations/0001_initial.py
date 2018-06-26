# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-19 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('EnName', models.CharField(default='xx', max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(db_index=True, max_length=32)),
                ('ip', models.GenericIPAddressField(db_index=True, protocol='IPV4')),
                ('port', models.IntegerField()),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.Business')),
            ],
        ),
    ]
