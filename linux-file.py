import os
import subprocess
os.system('uname')
os.system('date')
os.system('pwd')

if os.path.isdir("/python"):
    print("its directory")
else:
    print("its not directory")

uname="uname"
uname_arg="-a"
print(f"info of {uname} command")
subprocess.call([uname,uname_arg])

diskspace="df"
diskspace_arg="-h"
print(f"info of {diskspace} command")
subprocess.call([diskspace,diskspace_arg])

#instead of writing directly use the code inside function and call when necessary 
#instead of commenting multiple lines to not execute if we just comment funciton call its easy to mainatin too

def os_type():
    uname="uname"
    uname_arg="-a"
    print(f"info of {uname} command")
    subprocess.call([uname,uname_arg])

os_type()

#if we dont want to execute os type function just comment it


#glob module -- filename globbing utility

import glob

files=glob.glob('*.py') 
print(files) #it gives list as o/p


