#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 20:36
# @Author  : Dengsc
# @Site    : 
# @File    : tasks.py
# @Software: PyCharm


from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
