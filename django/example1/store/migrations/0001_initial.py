# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('teacher', models.CharField(max_length=255, null=True)),
                ('datetime', models.CharField(max_length=255, null=True)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fioStudent', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('healthGroup', models.IntegerField(default=0)),
                ('sectionStudent', models.ForeignKey(to='store.Section', null=True)),
            ],
        ),
    ]
