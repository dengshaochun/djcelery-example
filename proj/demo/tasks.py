#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 20:36
# @Author  : Dengsc
# @Site    : 
# @File    : tasks.py
# @Software: PyCharm


from __future__ import absolute_import, unicode_literals
from celery import shared_task

from demo.funcs.test_ansible import exec_playbook, exec_ad_hoc


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def test_celery_ansible_playbook():
    return exec_playbook('test_roles.yml')


@shared_task
def test_celery_ansible_ad_hoc():
    return exec_ad_hoc()
