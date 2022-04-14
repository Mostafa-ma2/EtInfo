#!/usr/bin/env python3

import socket
import threading
import sys
from lib.colors import colors

class port_scan:
    
    def __init__(self,ipAddress) :
        self.ipAddress= ipAddress
        self.threads = []
        self.result = {}
    
   
    def sock_conn(self,port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((self.ipAddress, int(port)))
            sock.close()
            service = socket.getservbyport(int(port), 'tcp')
            print(colors.Green + '[+] ' + colors.Cyan + str(port).ljust(7) + colors.White + service.ljust(9))
            self.result.update({str(port):service})
        except:
            sock.close()
            pass
    
    
    
    def thread_scan(self,port):
        t = threading.Thread(target=self.sock_conn, args=[port])
        t.daemon = True
        t.start()
        self.threads.append(t)
  
    def scan(self):
        
        
        ports = input('\n'+
            colors.Green + '[ + ] ' + colors.White + 'Please type porst (1-1024 or 1,2,3,...) '+colors.Cyan+': ')
        print('\n' + colors.Yellow + '[!]' + colors.Yellow + ' Starting Port Scan...' + colors.White + '\n')
        
        try:
            if ports.find('-') != -1:
                for port in range(int(ports.split('-')[0]),int(ports.split('-')[1])):
                    if isinstance(port,int) and port < 65536:
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
            
    