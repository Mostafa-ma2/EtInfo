#!/usr/bin/env python3

import ipwhois
from lib.colors import colors


class whois:

    def __init__(self, ip, data):
        self.ip = ip
        self.data = data

    def whois_lookup(self):
        collect = {}
        print('\n' + colors.Yellow +
              '[!]' + colors.Yellow + ' Whois Lookup : ' + colors.White + '\n')
        try:
            lookup = ipwhois.IPWhois(self.ip)
            results = lookup.lookup_whois()
            for k, v in results.items():
                if v != None:
                    if isinstance(v, list):
                        for item in v:
                            for k, v in results.items():
                                if v != None:
                                    print(colors.Green + '[+]' + colors.Cyan + ' {} : '.format(str(k)) + colors.White + str(
                                        v).replace(',', ' ').replace('\r', ' ').replace('\n', ' '))
                                    collect.update({str(k):str(v).replace(',', ' ').replace('\r', ' ').replace('\n', ' ')})
                                else:
                                    pass
                    else:
                         print(colors.Green + '[+]' + colors.Cyan + ' {} : '.format(str(k)) + colors.White + str(
                                        v).replace(',', ' ').replace('\r', ' ').replace('\n', ' '))
                         collect.update({str(k):str(v).replace(',', ' ').replace('\r', ' ').replace('\n', ' ')})
        except:
            pass
