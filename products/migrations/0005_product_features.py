# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-23 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180723_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=False),
        ),
    ]
