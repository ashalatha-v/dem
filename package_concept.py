"""packages
=======
-->collection of modules
-->if __init__ file is created under a folder then that folder is treated as package
init file is a initialising file--if init file isnt created then its created just like  folder---it contains module information

top level init file we need to edit and put the package and  properties present in modules

package name.modulename

in top level package only we need to mention sub modules info too



ex:
mymath/ ----------top level package
        ___init__.py ---in top level init file only we define sub package info too since it is best practice.
        sum.py
        adv/-------sub package
        __init__.py
        sub.py
        mult.py
    
"""

import mymath
x=int(input("enter num1: "))
y=int(input("enter num2: "))
print(f"sum of {x} and {y}: {mymath.add(x,y)}")
print(f"mult of {x} and {y}: {mymath.multiply(x,y)}")
print(f"sub of {x} and {y}: {mymath.subtract(x,y)}")
print(f"sub of {x} and {y}: {mymath.ad.sub.subtract(x,y)}") #it works but we cant include whole path of package generally not best practice
#print(f"sub of {x} and {y}: {mymath.sub.subtract(x,y)}") 
#AttributeError: module 'mymath' has no attribute 'sub' as sub file is in ad package its throwing attribute error
print(f"sub of {x} and {y}: {mymath.ad.subtract(x,y)}")  #AttributeError: module 'mymath' has no attribute 'sub'
 #before adding import statements of pa ckage in ad init file we get error sayin attribute error
#after adding we get o/p

#note:
#usually we dont add import statemnts in sub package init file


#packagename.propertyname()


#working with json with python
#if we use help(any module)
# and find file location is __init__.py,then its a package


