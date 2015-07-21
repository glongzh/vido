#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import re
from hashlib import md5
from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from .models import Item, Task

# Create your views here.


def index(req):
    tasks = []
    sid = req.session.get('session_id', '')
    if not sid:
        req.session['session_id'] = uuid.uuid1().hex
    else:
        tasks = Task.objects.filter(
            session_id=sid).order_by('-created_at')[:50]

    c = {}
    c.update(csrf(req))
    if tasks:
        c.update({'tasks': tasks})
    return render_to_response('index.html', c, context_instance=RequestContext(req))


def submit(req):
    ytv_pattern = '(?:http|https|)(?::\/\/|)(?:www.|)(?:youtu\.be\/|youtube\.com(?:\/embed\/|\/v\/|\/watch\?v=|\/ytscreeningroom\?v=|\/feeds\/api\/videos\/|\/user\S*[^\w\-\s]|\S*[^\w\-\s]))([\w\-]{11})[a-z0-9;:@#?&%=+\/\$_.-]*'
    url = req.POST.get('url', '').strip()
    sid = req.session.get('session_id')
    if url:
        m = re.match(ytv_pattern, url)
        if True:
            vid = m.group(1)
            site = 'youtube'
            md5 = get_md5(site, vid)
            need_pushing = True if req.POST.get('push') else False
            item, created = Item.objects.get_or_create(
                md5=md5, url=url, site=site)
            if created:
                t = Task.objects.create(session_id=sid, url=url, item=item, need_pushing=need_pushing)
                t.save()
                return redirect_index_with_msg(req, '下载任务添加成功')
            else:
                # display exist task or downloaded link
                try:
                    t = Task.objects.get(session_id=sid, url=url, status='failed')
                    t.status = 'queue'
                    t.save()
                    return redirect_index_with_msg(req, '重新开始下载任务')
                except ObjectDoesNotExist:
                    return redirect_index_with_msg(req, '下载任务已存在')
                
        else:
            return redirect_index_with_msg(req, '不支持的下载链接')
    else:
        return redirect_index_with_msg(req, '下载链接不能为空')


def redirect_index_with_msg(req, msg):
    messages.info(req, msg)
    return redirect(reverse(index))


def get_md5(site, vid):
    m = md5()
    m.update(site + vid)
    return m.hexdigest()
