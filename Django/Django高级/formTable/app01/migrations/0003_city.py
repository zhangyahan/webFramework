# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-18 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20181217_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'db_table': 'city_name',
            },
        ),
    ]
