# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('uncertainty', models.DecimalField(decimal_places=2, max_digits=100)),
                ('brand', models.CharField(blank=True, max_length=255)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=100)),
                ('Available', models.BooleanField(default=True)),
            ],
        ),
    ]
