# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='user_id',
        ),
    ]
