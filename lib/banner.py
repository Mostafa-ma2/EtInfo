#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : EtInfo - Extract Info
# @url    : https://github.com/Mostafa-ma2
# @group : system-smashers

from re import A
from colorama import Fore

class Banner():
    def __init__(self):
        pass
    def banner(self):
        print(Fore.GREEN+u"""  \x1b[36m╔════════════════════════════════════════════════════════════════════════╗\x1b[36m
              ║ \x1b[36m            ███████╗████████╗██╗███╗   ██╗███████╗ ██████╗             ║ \x1b[36m
              ║ \x1b[36m            ██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝██╔═══██╗            ║ \x1b[36m
              ║ \x1b[36m            █████╗     ██║   ██║██╔██╗ ██║█████╗  ██║   ██║            ║ \x1b[36m
              ║ \x1b[36m            ██╔══╝     ██║   ██║██║╚██╗██║██╔══╝  ██║   ██║            ║ \x1b[36m
              ║ \x1b[36m            ███████╗   ██║   ██║██║ ╚████║██║     ╚██████╔╝            ║ \x1b[36m
              ║ \x1b[36m            ╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝             ║ \x1b[36m
              ╚═════════════╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦══════════════╝
                            ║S║y║s║t║e║m║ ║ ║ ║ ║ ║ ║ ║ ║S║m║a║s║h║e║r║s║ 
                          ╔═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╗
                          ║\x1b[33m Channel : SystemSmashers\x1b[36m                      ║
                          ║\x1b[33m Developers : Mostafa Abedini\x1b[36m                  ║
                          \x1b[36m╚═══════════════════════════════════════════════╝\x1b[36m
                          \n\x1b[37m  OPTIONS:\n
                          \n\t\x1b[40m(1)\x1b[0m\x1b[37m  Whois\n
                          \n\t\x1b[40m(0)\x1b[0m\x1b[37m  Exit\n""")
    
    def usage(self):
        pass
    
Banner.banner("s")