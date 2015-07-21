# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vidown', '0005_auto_20150716_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 19, 8, 2, 16, 302583), auto_now=True),
            preserve_default=False,
        ),
    ]
