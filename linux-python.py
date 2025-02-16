#working with linux

"""
modules 

os,subprocess,sys

"""
import subprocess #in built 
#print(dir(subprocess))

import os #in built module
#print(dir(os))


#virtual-box meaning hypervisor where we can put multiple virtual machine on it and each VM equals to 1 operating system

#how to write python script on linux os
"""
open terminal
=============
python -v

open any text editor
==================
1. vi
2. nano
3. ed

vi scriptname.py
================
write python code

:wq save and exit
:w save
:q exit

how to excecute 
============
python scriptname.py


if we need to use options along with command we need to use subprocesses

"""
"""unix-paid os
linus torvalde developed linux with providing free os with unix features,secure,open source,"""

import os
if os.path.isfile('./json_file.py'):
    print("yes")
else:
    print("no")

import subprocess
print(dir(subprocess))
print(help(subprocess))

