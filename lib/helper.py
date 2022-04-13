#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# @name   : EtInfo - Extract Info
# @url    : https://github.com/Mostafa-ma2
# @another : Mostafa Abedini(Mostafa-ma2)

import os
import requests
import sys
import json
import importlib.util
import socket

from lib.colors import colors


class helper:

    def __init__(self, app_version=None):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.app_version = app_version
        self.socket_timeout = 3
        self.socket_port = 53
        self.socket_ip = "8.8.8.8"

    def clear(self):
        if os.uname().sysname.lower() in "win":
            os.system("cli")
        else:
            os.system("clear")

    def pkg_install(self):
        fail = True
        with open(self.path + '/requirements.txt', 'r') as rqr:
            pkg_list = rqr.read().strip().split("\n")
        for pkg in pkg_list:
            spec = importlib.util.find_spec(pkg)
            if spec is None:
                print(colors.Red + '[-]' + colors.White + ' {}'.format(pkg) +
                      colors.Cyan + ' is not Installed!' + colors.White)
                fail = False
            else:
                pass
        if fail == False:
            print('\n' + colors.Red + '[-]' + colors.Cyan + ' Please Execute ' + colors.White +
                  'pip3 install -r requirements.txt' + colors.Cyan + ' to Install Missing Packages' + colors.White + '\n')
            sys.exit()

    def check_internet(self):
        try:
            socket.setdefaulttimeout(self.socket_timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                self.socket_ip, self.socket_port)
            pass
        except socket.error as ex:
            print('\n' + colors.Red +
                  '[-]' + colors.White+'Please chack your Internet ....\n')
            sys.exit()

    def check_update(self):
        version = ""
        try:
            rqst = requests.get(
                'https://raw.githubusercontent.com/Mostafa-ma2/EtInfo/main/metadata.json', timeout=5)
            if rqst.status_code == 200:
                metadata = rqst.text
                version = json.loads(metadata)['metadata']['version']

            else:
                with open('metadata.json', 'r') as metadata:
                    version = json.loads(metadata.read())[
                        'metadata']['version']
        except Exception as exc:
            print('\n' + colors.Red + '[-]' + colors.Cyan +
                  ' Exception : ' + colors.White + str(exc))
            with open('metadata.json', 'r') as metadata:
                version = json.loads(metadata.read())['metadata']['version']

        print(colors.Green + '[+]' + colors.Cyan +
              ' Checking for Updates...', end='')
        if version == self.app_version:
            print(colors.Cyan + '[' + colors.Green +
                  ' Up-To-Date ' + colors.Cyan + ']' + '\n')
        else:
            print(
                colors.Cyan + '[' + colors.Green + ' Available : {} '.format(version) + colors.Cyan + ']' + '\n')
