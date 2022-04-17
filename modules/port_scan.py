#!/usr/bin/env python3

import socket
import threading
import sys
from lib.colors import colors


class port_scan:

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
        self.threads = []
        self.result = []
        self.protocol = 'udp'

    def sock_conn(self, port):
        try:
            sock = socket

            if self.protocol == 'tcp': 
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect_ex((self.ipAddress, int(port)))
            elif self.protocol == 'udp':
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for x in range(500):
                    sock.sendto(('RST').encode('utf_8'),(self.ipAddress,int(port)))
            sock.settimeout(3)
            sock.close()
            service = socket.getservbyport(int(port), self.protocol)
            output=''+colors.Green + '[+] ' + colors.Cyan + str(port)+'/'+self.protocol.ljust(5)+ colors.White + service.ljust(9)+''
            print(output)
            self.result.append(output)
        except:
            sock.close()
            pass

    def thread_scan(self, port):
        t = threading.Thread(target=self.sock_conn, args=[port])
        t.daemon = True
        t.start()
        self.threads.append(t)

    def scan(self):
        
        self.protocol = input('\n' +
                      colors.Green + '[ + ] ' + colors.White + 'Please type protocol (tcp/udp) '+colors.Cyan+': ')
        ports = input('\n' +
                      colors.Green + '[ + ] ' + colors.White + 'Please type porst (1-1024 or 1,2,3,...) '+colors.Cyan+': ')
        print('\n' + colors.Yellow + '[!]' + colors.Yellow +
              ' Starting port scanning ...' + colors.White + '\n')

        try:
            if ports.find('-') != -1:
                for port in range(int(ports.split('-')[0]), int(ports.split('-')[1])):
                    if isinstance(port, int) and port < 65536:
                        self.thread_scan(port=port)
            else:
                for port in ports.split(','):
                    if int(port) < 65536:
                        self.thread_scan(port=int(port))

        except:
            print('\n' + colors.Red + '[-] Error :' + colors.White +
                  ' Please check your port ' + colors.Cyan + '!\n')
            sys.exit()
        for thread in self.threads:
            thread.join()
        
        return self.result
