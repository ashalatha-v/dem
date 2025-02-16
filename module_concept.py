"""
module is collection of functions,executable statememts,variables
just another python script
module extension is also .py
every python file we can treat as a module

types of modules:
1. built in modules:
comes with python 
in lib folder we get built in modules
2.user defined module or custom module: created by user
under current working directory we create our own modules
3. third party modules
(PyPI)-python package index is a repository we get third party module
under lib we ahve site-packages in that folder we get to see third party packages or modules 


pip(package manager) is tool to install and manage package or modules
 install pandas we use pip install pandas
 to show details about package installed via pip we use pip show pandas 
 
 package is nothing collection of modules

 #priority for checking modules
 user defined or custom modules--->built in modules(lib folder)--> third party modules(site-packages)
 if not found in any the module then error
 


 import module
 print(dir(module))-- display properties of a mentioned module
 print(help(module))-- display documenetation

"""

#how to access module properties(functions or varaibles):
"""
1. import modulename(import all properties i 1 single import statement)
and later use modulename.propertyname()

2. from modulename import propertyname
here we import only 1 property from a given module
we can directly use propertyname() --- only 1

or
from modulename import propertyname1,propertyname2,propertyname3
propertyname1()
propertyname2()
propertyname3()

or 
from modulename import *



import math
import arithmetic
x=int(input("enter a number to get square root"))
print(f"square root of {x} is {math.sqrt(x)}")
print(dir(arithmetic))
print(help(arithmetic))

how to import alias for modulename

import modulename as aliasname

ex:
import pandas as pd
import statistic as stat

once alias is defined,we need to use alais name only

module search path:
current working directory--> lib folder(built in modules)--> third party (site-packages folder)
"""

#import of .pyc File:
"""
1.for each module or py file, after wr import any module for first time,then __pycache__ folder is created---> 
under that folder,.pyc(compiled python file) file is created for .py file

pyc file(compiled python file ) is nothing but a binary file first timw when module is imported it verifies syntax,it all syntax is correct, .pyc file is craeted

from .pyc file ,executing starts

2.when second time we import, it comapres py and .pyc file since no change it proceedes with exisiting .pyc file

3. when we import again with few changes in module or .py file again it will create new .pyc file


how to install third party modules:

1.pip install modulename-- collects modules and its dependencies if necessary

2. easy_install modulename-- instal only module specified to intall no dependencies

where Lib folder exists , see for Scipts folder-->under that easy-intsall and pip install

if no scripts folder path in python then we get pip not recognised
pip not recognised because whether the path is set to environment variable or not
to check that go for this pc--> properties--> search for environment variables


after installation of module how to verify
==========================================
pip show modulename

how to uninstall module
======================
pip uninstall modulename

how to list all the modules or packages installed via pip
======================
pip list|more
pip freeze|more

how to intall a module with specifying the version
==============================================
pip install modulename==version

pip install pandas==2.0.1

ex:if we have installed module but it doesnt match with our requirement
then we need to unintall and again install by specifiying version

when we try to upgrade a module it will automatically uninstall the modules which wont match with current installing module


if function we need is locally present in the current .py file it wont go for import sattement to check if function we need is in module 
and also if function call searching a function, if we r searching occurs first before searching in import module then local function is executed and return value
so anywhere local is important

from arithmatic import *
from pandas import *
def sum(a,b):
    return 100

sum(10,20) #here 135 is executed


from pandas import *
def sum(a,b):
    return 100
from arithmatic import *

sum(10,20) #here 144 is executed as we get 144 we get first as we follow bottom-top approach for function call execution

so solution would be giving alias name and use alias name.call property
so even local function is occured 

import arithmetic as arith
from math import *
def sum(a,b):
    return 100
from arithmatic import *

arith.sum(10,20) #now it will only take function math() from module arithmetic or alias arith

just file .py is a module
folder is a package

#executing module as script
___name__ is a speciable variable which can be to execute or perform an function only if it is called as main fucntion (based on where that function is called )








"""