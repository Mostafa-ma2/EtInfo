#!/usr/bin/env python

import sys
import os
import time
import importlib.util

from lib.colors import colors
# ----------  Variables  ---------------
is_running = True  # project has running
app_version = "1.0.0"  # app version
data = {}
project_path = os.path.dirname(os.path.realpath(__file__))


def main():
    global is_running
    option = input(colors.Green+'[' + format(time.strftime("%H:%M:%S", time.localtime()
                                                           )) + ']' + colors.White+' Please select an option ' + colors.Cyan+': ')
    if option != '3' and option.lower() != "dns record":
        ip_address = get_ipAddress('ip/website')

    if option == "1" or option.lower() == "whois":
        whois(helper(None, ip_address).check_ipAdress(), data).whois_lookup()

    elif option == "2" or option.lower() == "port scan":
        port_scan(ipAddress=helper(None, ip_address).check_ipAdress()).scan()

    elif option == "3" or option.lower() == "dns record":
        ip_address = get_ipAddress('website')
        dns_record(ipAddress=helper(
            None, ip_address).check_domain()).dnsrec()

    if option == "0" or option.lower() == "exit":
        do_want = 'no'
    else:
        do_want = input('\n'+colors.Green+'[' + format(time.strftime("%H:%M:%S", time.localtime()
                                                                     )) + ']' + colors.White+' Do you want to continue?(y/n) ' + colors.Cyan+': ')
    if do_want.lower() == "n" or do_want.lower() == "no":
        print('\n'+colors.Green + '[ + ]' +
              colors.White + ' Good luck '+colors.Cyan+'! ')
        is_running = False


def pkg_install(path):
    fail = True
    with open(path + '/requirements.txt', 'r') as rqr:
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


def get_ipAddress(txt):
    return input('\n' +
                 colors.Green + '[ + ] ' + colors.White + 'Please type ('+txt+') '+colors.Cyan+': ')


if __name__ == "__main__":
    pkg_install(project_path)

    # --------- import file ----------------
    from lib.helper import helper
    from lib.banner import banner
    from modules.whois import whois
    from modules.port_scan import port_scan
    from modules.dns_record import dns_record
    helper().check_internet()  # check internet connection
    while is_running:
        helper().clear()  # cleen terminal
        banner.banner()
        main()
