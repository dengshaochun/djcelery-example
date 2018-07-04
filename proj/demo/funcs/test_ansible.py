#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 20:58
# @Author  : Dengsc
# @Site    : 
# @File    : test_ansible.py
# @Software: PyCharm

import os
from proj import settings
from utils.myAnsible.myPlaybookRunner import PlaybookRunner
from utils.myAnsible.myRunner import Runner


def exec_playbook(playbook):
    host_dict = {
        'group1': {
            'hosts': ['test01', 'test02'],
            'vars': {'ansible_ssh_user': 'dengsc', 'ansible_ssh_pass': '119335'}
        },
        '_meta': {
            'hostvars': {
                'test01': {
                    'zone_dirs': ['/home/dengsc', ]
                }
            }
        }
    }

    runner = PlaybookRunner(
        playbook_path=os.path.join(settings.PLAYBOOKS_PATH, playbook),
        hosts=host_dict
    )

    result = runner.run()
    return result


def exec_ad_hoc():
    hosts_dict = {
        'tmp_ad_hoc': {
            'hosts': ['test01', 'test02'],
        }
    }

    runner = Runner(
        module_name='setup',
        remote_user=settings.DEFAULT_ANSIBLE_USER,
        pattern='tmp_ad_hoc',
        private_key_file=settings.DEFAULT_ANSIBLE_PRIVATE_KEY,
        hosts=hosts_dict,
    )
    result = runner.run()
    return result
