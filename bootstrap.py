#!/usr/bin/env python
# File heavily inspired by: http://github.com/thraxil/ccdb/blob/9d72e9f7baf641e43c135237c858e23f75646f29/bootstrap.py
import os
import sys
import subprocess
import shutil
 
PWD = os.path.dirname(__file__)
# give our  virtualenv a descriptive name:
VEDIR = os.path.join(PWD, "nimbus-web-portal-env")

#allow use local (bundled) bin/virtualenv.py:
sys.path.insert(0, os.path.join(PWD, "bin/"))
 
if os.path.exists(VEDIR):
    shutil.rmtree(VEDIR)
 
PIP = os.path.join(PWD, "bin/pip.py")
REQUIRE = os.path.join(PWD, "requirements/apps.txt")
subprocess.call([PIP, "install", "-E", VEDIR, "--requirement", REQUIRE])

