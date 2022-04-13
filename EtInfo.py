#!/usr/bin/env python

import sys
import os
import atexit
import time



from lib.helper import helper
from lib.colors import colors
from lib.banner import banner
from modules.whois import whois

# ----------  Variables  ---------------
is_running = True  # project has running
app_version = "1.0.0" # app version
data = {}

def main():
    global is_running
    option = input(colors.Green+'[' + format(time.strftime("%H:%M:%S", time.localtime()
                                                           )) + ']' + colors.White+' Please select an option ' + colors.Cyan+': ')
    if option == "1" or option.lower() == "whois":
        ip_address = input(
            colors.Green + '[ + ]' + colors.White + 'Please type (ip/website) '+colors.Cyan+': ')
        whois(helper(None,ip_address).check_ipAdress(),data).whois_lookup()
    
    
    if option == "0" or option.lower() == "exit":
        do_want=False
    else:
        do_want=input('\n'+colors.Green+'[' + format(time.strftime("%H:%M:%S", time.localtime()
                                                           )) + ']' + colors.White+' Do you want to continue?(y/n) ' + colors.Cyan+': ')
    if do_want.lower() == "n" or do_want.lower() == "no":
        print('\n'+colors.Green + '[ + ]' + colors.White + 'Good luck '+colors.Cyan+'! ')
        is_running  = False


if __name__ == "__main__":
    helper().pkg_install()
    helper().check_internet()
    while is_running:
        helper().clear()
        banner.banner()
        main()
