# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vidown', '0003_auto_20150705_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quality',
            field=models.CharField(default=b'h', max_length=10, choices=[(b'h', b'High'), (b'm', b'Medium'), (b'l', b'Low')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'queue', max_length=30, choices=[(b'queue', '\u6392\u961f\u4e2d'), (b'downloading', '\u4e0b\u8f7d\u4e2d'), (b'failed', '\u4e0b\u8f7d\u5931\u8d25'), (b'success', '\u4e0b\u8f7d\u6210\u529f'), (b'pushing', '\u63a8\u9001\u4e2d'), (b'pushed', '\u63a8\u9001\u5b8c\u6210'), (b'pushing_failed', '\u63a8\u9001\u5931\u8d25')]),
        ),
    ]
