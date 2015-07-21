#!/usr/bin/python
#  -*- coding: utf-8 -*-

import os
from django.db import models
from django.conf import settings

# Create your models here.
STATUS_CHOICES = (
    ('queue', u'排队中'),
    ('downloading', u'下载中'),
    ('failed', u'下载失败'),
    ('success', u'下载成功'),
    ('pushing', u'推送中'),
    ('pushed', u'推送完成'),
    ('pushing_failed', u'推送失败')
)

QUALITY_CHOICES=(
	('h','High'),
	('m', 'Medium'),
	('l', 'Low')
)

class Item(models.Model):

    """Download item"""

    md5=models.CharField(max_length=40, unique=True)
    url=models.CharField(max_length=200)
    title=models.CharField(max_length=500, blank=True)
    desc=models.TextField(blank=True)
    quality=models.CharField(max_length=10, choices=QUALITY_CHOICES, default='h')
    file_size=models.IntegerField(default=0)
    ext=models.CharField(max_length=10, blank=True, default='mp4')
    site=models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.get_item_filename()

    def get_item_path(self):
        return settings.SAVE_PATH + self.get_item_filename()

    def get_item_filename(self):
        return self.md5 + '.' + self.ext

    def file_exist(self):
        return os.path.exists(self.get_item_path())

    def delete_files(self):
        if self.file_exist():
            try:
                os.remove(self.get_item_path())
                os.remove(os.path.splitext(self.get_item_path())[0] + '.info.json')
            except:
                pass
            

class Task(models.Model):

    """Download task"""

    session_id = models.CharField(max_length=255)
    url = models.CharField(max_length=1000)
    item = models.ForeignKey(Item)
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default='queue')
    need_pushing = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url


