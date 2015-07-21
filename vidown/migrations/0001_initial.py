# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('md5', models.CharField(unique=True, max_length=40)),
                ('url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500, blank=True)),
                ('desc', models.TextField(blank=True)),
                ('quality', models.CharField(default=b'M', max_length=10, choices=[(b'h', b'High'), (b'm', b'Medium'), (b'l', b'Low')])),
                ('file_size', models.IntegerField()),
                ('ext', models.CharField(max_length=10)),
                ('site', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=500)),
                ('status', models.CharField(default=b'Queue', max_length=30, choices=[(b'queue', '\u6392\u961f\u4e2d'), (b'downloading', '\u4e0b\u8f7d\u4e2d'), (b'failed', '\u4e0b\u8f7d\u5931\u8d25'), (b'success', '\u4e0b\u8f7d\u6210\u529f'), (b'pushing', '\u63a8\u9001\u4e2d'), (b'pushed', '\u63a8\u9001\u5b8c\u6210'), (b'pushing_failed', '\u63a8\u9001\u5931\u8d25')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(to='vidown.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
