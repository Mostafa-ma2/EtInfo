#!/usr/bin/env python

import sys
import os 
import atexit
from lib.helper import helper
from lib.banner import banner
# ----------  Variables  ---------------
is_running= True # project has running



if __name__ == "__main__":
    if is_running:
        helper.clear()
        banner.banner()
        