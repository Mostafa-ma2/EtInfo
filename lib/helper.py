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
import socket
import whois
from IPy import IP
from lib.colors import colors


class helper:

    def __init__(self, app_version=None, ip_address=None):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.app_version = app_version
        self.socket_timeout = 3
        self.socket_port = 53
        self.socket_ip = "8.8.8.8"
        self.ipAddress = ip_address

    def clear(self):
        if os.uname().sysname.lower() in "win":
            os.system("cli")
        else:
            os.system("clear")

    def check_internet(self):
        try:
            socket.setdefaulttimeout(self.socket_timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (self.socket_ip, self.socket_port))
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

    def check_ipAdress(self):
        try:
            IP(self.ipAddress)
            return(self.ipAddress)
        except:
            try:
                return socket.gethostbyname(self.ipAddress)
            except:
                print('\n' + colors.Red + '[-] Error :' + colors.White +
                      ' Please check your ip/website ' + colors.Cyan + '!\n')
                sys.exit()

    def check_domain(self):
        
        s=whois.whois(self.ipAddress)
        if whois.whois(self.ipAddress).domain_name != None:
            return self.ipAddress

        try:
            host = socket.gethostbyaddr(self.ipAddress)
            if len(host[2]) != 0:
                sys.exit()

            return(host)
        except:
            print('\n' + colors.Red + '[-] Error :' + colors.White +
                  ' Please check your website ' + colors.Cyan + '!\n')
            sys.exit()
