#!/usr/bin/python
# -*- coding:utf-8 -*-

# Copyright(C) 2023 Kaytus Inc. All Rights Reserved.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
module: connect_media_info
version_added: "1.0.0"
author:
    - WangBaoshan (@ieisystem)
short_description: Get remote images redirection information
description:
   - Get remote images redirection information on kaytus Server.
notes:
   - Supports C(check_mode).
options: {}
extends_documentation_fragment:
    - kaytus.ksmanage.ksmanage
'''

EXAMPLES = '''
- name: Connect media test
  hosts: ksmanage
  connection: local
  gather_facts: no
  vars:
    ksmanage:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Get remote images redirection information"
    kaytus.ksmanage.connect_media_info:
      provider: "{{ ksmanage }}"
'''

RETURN = '''
message:
    description: Messages returned after module execution.
    returned: always
    type: str
state:
    description: Status after module execution.
    returned: always
    type: str
changed:
    description: Check to see if a change was made on the device.
    returned: always
    type: bool
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.kaytus.ksmanage.plugins.module_utils.ksmanage import (ksmanage_argument_spec, get_connection)


class Connect(object):
    def __init__(self, argument_spec):
        self.spec = argument_spec
        self.module = None
        self.init_module()
        self.results = dict()

    def init_module(self):
        """Init module object"""

        self.module = AnsibleModule(
            argument_spec=self.spec, supports_check_mode=True)

    def run_command(self):
        self.module.params['subcommand'] = 'getconnectmedia'
        self.results = get_connection(self.module)

    def show_result(self):
        """Show result"""
        self.module.exit_json(**self.results)

    def work(self):
        """Worker"""
        self.run_command()
        self.show_result()


def main():
    argument_spec = dict()
    argument_spec.update(ksmanage_argument_spec)
    connect_obj = Connect(argument_spec)
    connect_obj.work()


if __name__ == '__main__':
    main()