import os
import requests
import sys
import importlib.util


from lib.colors import colors

class helper:
    
    def __init__(self,app_version=None):
        self.path= os.path.dirname(os.path.realpath(__file__))
        self.app_version=app_version
    
    def clear(self):
        if os.uname().sysname.lower() in "win":
            os.system("cli")
        else:
            os.system("clear")
    
    def pkg_install(self):
        fail = True
        with open(self.path + '/requirements.txt', 'r') as rqr:
            pkg_list=rqr.read().strip().split("\n")
        for pkg in pkg_list:
            spec= importlib.util.find_spec(pkg)
            if spec is None:
                print(colors.Red + '[-]' + colors.White + ' {}'.format(pkg) + colors.Cyan + ' is not Installed!' + colors.White)
                fail = False
            else:
                pass
        if fail == False:
            print('\n' + colors.Red + '[-]' + colors.Cyan + ' Please Execute ' + colors.White + 'pip3 install -r requirements.txt' + colors.Cyan + ' to Install Missing Packages' + colors.White + '\n')
            sys.exit()
 