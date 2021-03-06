# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-18 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fstaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('gender', models.CharField(max_length=32)),
                ('u2g', models.ManyToManyField(to='myapp.DepartmentGroup')),
            ],
        ),
        migrations.CreateModel(
            name='FuserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32, unique=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(error_messages={'invalid': '格式错误', 'required': '不能为空.'}, max_length=32, null=True)),
                ('user_type_id', models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '垃圾用户')], default=1)),
                ('user_group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.UserGroup')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='ut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserType'),
        ),
        migrations.AddField(
            model_name='fstaff',
            name='ut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.FuserType'),
        ),
    ]
