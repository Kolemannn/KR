# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField()),
                ('attendance', models.BooleanField()),
                ('reason', models.CharField(max_length=255, default='Укажите причину')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('datetime', models.CharField(max_length=255, null=True)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fioStudent', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('healthGroup', models.IntegerField(default=0)),
                ('contStudent', models.CharField(max_length=255)),
                ('sectionStudent', models.ForeignKey(null=True, to='store.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fioTeacher', models.CharField(max_length=255)),
                ('sport', models.CharField(max_length=255)),
                ('contTeacher', models.CharField(max_length=255)),
                ('trackRecord', models.CharField(max_length=255)),
                ('grade', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='teacher',
            field=models.ForeignKey(null=True, to='store.Teacher'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='studentAttend',
            field=models.ForeignKey(null=True, to='store.Student'),
        ),
    ]
