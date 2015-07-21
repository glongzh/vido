#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: glongzh

import re

def sanitize(str, replace=''):
	str = re.sub(r'[\/\?<>\\:\*\|":]', replace, str)
	str = re.sub(r'[\x00-\x1f\x80-\x9f]', replace, str)
	str = re.sub(r'^\.+$', replace, str)
	str = re.sub(r'^(con|prn|aux|nul|com[0-9]|lpt[0-9])(\..*)?$', replace, str, flags=re.I)
	return str
