#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'glongzh'

import os, sys, time, subprocess, json, datetime
from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "vido.settings"
sys.path.append("/Users/glongzh/Projects/vido") # add project folder to sys path
import django
django.setup()

from django.db.models import Q
from vidown.models import Task, Item
from bypy import ByPy
from utils import sanitize



def clean():
    now = datetime.datetime.utcnow()
    max_life_time = datetime.timedelta(hours=settings.SAVED_LIFETIME)
    tasks = Task.objects.all()
    for t in tasks:
        life_time = now - t.updated_at.replace(tzinfo=None)
        if life_time > max_life_time and t.item.file_exist():
            t.item.delete_files()
            t.delete()


def resume_pushing():
    pushing_tasks = Task.objects.filter(status='pushing')
    if pushing_tasks:
        pcs = ByPy()
        for pt in pushing_tasks:
            if pt.item.file_exist():
                push_res = pcs.upload(pt.item.get_item_path(), sanitize(pt.item.title) + '.mp4')
                print 'push_res:' + str(push_res)
                if push_res == 0 or push_res == 60:
                    pt.status = 'pushed'
                    os.remove(pt.item.get_item_path())
                else:
                    pt.status = 'pushing_failed'
                pt.save()


def download():
    cmd_fmt = "{0} -i -R 2 --write-info-json -o '{1}' {2}"
    tasks = Task.objects.filter(Q(status='queue') | Q(status='downloading')).order_by('created_at')

    if tasks:
        pcs = ByPy()
        for t in tasks:
            item = t.item
            cmd = cmd_fmt.format(settings.YTDL_PATH, item.get_item_path(), item.url)
            t.status = 'downloading'
            t.save()
            print 'execute command:' + cmd
            ret = subprocess.call(cmd,shell=True)
            if item.file_exist():
                meta_file_path = os.path.join(settings.SAVE_PATH, item.md5 + '.info.json')
                with open(meta_file_path, 'r') as f:
                    meta = json.load(f)
                    item.title = meta.get('title')
                    item.desc = meta.get('description')
                    item.save()
                t.status = 'success'
                t.save()
                if t.need_pushing:
                    t.status = 'pushing'
                    t.save()
                    push_res = pcs.upload(item.get_item_path(), sanitize(item.title) +'.mp4')
                    print 'push result:' + str(push_res)
                    if push_res == 0:
                        t.status = 'pushed'
                        os.remove(item.get_item_path())
                    else:
                        t.status = 'pushing_failed'
                    t.save()
                
            else:
                t.status = 'failed'
                t.save()

def work():
    while True:
        clean()
        resume_pushing()
        download()
        time.sleep(0.2)


if __name__ == '__main__':
	work()