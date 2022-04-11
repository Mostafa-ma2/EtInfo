import os

class helper:
    
    def __init__(self):
        pass
    
    def clear():
        if os.uname().sysname.lower() in "win":
            os.system("cli")
        else:
            os.system("clear")