# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-10 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='token',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
