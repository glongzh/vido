#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: glongzh

from django.test import TestCase
from utils import sanitize

# Create your tests here.
class UtilsTest(TestCase):
	def test_sanitize(self):
		str1 = 'Daniel Radcliffe Was Our Receptionist for an Hour'
		self.assertEqual(sanitize(str1), str1)
		
		str2 = 'Do you like her?'
		self.assertEqual(sanitize(str2), 'Do you like her')
