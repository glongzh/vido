# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vidown', '0004_auto_20150715_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='need_pushing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='ext',
            field=models.CharField(default=b'mp4', max_length=10, blank=True),
        ),
    ]
