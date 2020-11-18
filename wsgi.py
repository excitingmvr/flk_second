# -- coding: utf-8 --

import sys
import platform

if platform.system() == 'Windows':
    sys.path.insert(0, 'D:/factory/workspace_flask/flk_second')
elif platform.system() == 'Linux':
    sys.path.insert(0, '/factory/workspace_flask/flk_second')
    activate_this = '/factory/workspace_flask/flk_second/venv/bin/activate_this.py'
    execfile(activate_this, dict(__file__=activate_this))
else:   # mac (Darwin)
    sys.path.insert(0, '/factory/workspace_flask/flk_second')

from app import app as application