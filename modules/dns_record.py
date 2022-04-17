#!/usr/bin/env python3

import os
import dnslib
import dns
import dns.resolver

from lib.colors import colors


class dns_record:

    def __init__(self, ipAddress):
        self.ip_address = ipAddress
        self.result = []

    def dnsrec(self):
        self.type = input('\n' +
                          colors.Green + '[ + ] ' + colors.White + 'Please type DNS scan type (A,AAAA,TXT,MX,ANY,CAA,CNAME,NS) '+colors.Cyan+': ')

        print('\n' + colors.Yellow + '[!]' + colors.Yellow +
              ' Starting DNS Enumeration...' + colors.White + '\n')

        full_answer = []

        for type in self.type.split(','):
            question = dnslib.DNSRecord.question(str(self.ip_address), type.upper())
            send_pkt = question.send('8.8.8.8', 53, tcp='UDP')
            answer = dnslib.DNSRecord.parse(send_pkt)
            answer = str(answer)
            answer = answer.split('\n')
            full_answer.extend(answer)
            
        full_answer = set(full_answer)
        dns_found = []

        for entry in full_answer:
            if entry.startswith(';') == False:
                dns_found.append(entry)
            else:
                pass

        if len(dns_found) != 0:
            for entry in dns_found:
                out = colors.Green + '[+]' + colors.Cyan + \
                    ' {}'.format(entry) + colors.White
                print(out)
                self.result.append(out)
        else:
            print(colors.Red + '[-]' + colors.Cyan +
                  ' DNS Records Not Found!' + colors.White)
        
        return self.result
