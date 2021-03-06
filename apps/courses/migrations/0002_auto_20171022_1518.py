# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-22 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': '\u7ae0\u8282', 'verbose_name_plural': '\u7ae0\u8282'},
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '\u521d\u7ea7'), ('zj', '\u4e2d\u7ea7'), ('gj', '\u9ad8\u7ea7')], max_length=4, verbose_name='\u7b49\u7ea7'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u89c6\u9891\u540d'),
        ),
    ]
