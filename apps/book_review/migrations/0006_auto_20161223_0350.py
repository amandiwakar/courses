# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 03:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0005_auto_20161223_0349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='reviwer',
            new_name='reviewer',
        ),
    ]
