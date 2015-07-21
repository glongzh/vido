# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vidown', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AlterField(
            model_name='item',
            name='ext',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='file_size',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='site',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
