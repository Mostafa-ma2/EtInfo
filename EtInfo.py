#!/usr/bin/env python

import sys
import os 
import atexit
from lib.helper import helper
from lib.banner import banner
# ----------  Variables  ---------------
is_running= True # project has running
app_version="1.0.0"

if __name__ == "__main__":
    helper().pkg_install()
    helper(app_version).check_update()
    if is_running:
        helper().clear()
        banner.banner()
        