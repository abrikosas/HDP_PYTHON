#!/usr/bin/env python

import sys
from lib.command import Executor


c=Executor(sys.argv[1])

print(c.execute_os_command())


