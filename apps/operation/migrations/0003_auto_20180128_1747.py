# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-28 17:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20171021_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecomment',
            old_name='comment',
            new_name='comments',
        ),
    ]
