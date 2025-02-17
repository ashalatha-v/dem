import arithmetic
"""functions or procedures or sub-routines:
function are basically meant for reusability
only when functions are called,they will be executed

1. built in functions:
we have a module to get built in functions ie builtins
print(dir(__builtins__))
ex: for built in functions: len(),type(),print()...

2. user defined functions:
created by user to perform their own operation
using functions we can reduce code length
after function is defined,its should be called
but in programming lanuage,function call searches for function defintion in whole program 

def functionname():called function
    ---
    --

functionname()--calling function
"""
#print(dir(__builtins__))

print("hello")
#f1() #name f1 is not defined
def f2():
    """doc string""" #defining purpose of function f1() and also satrt and end with """ "
    print("world")
    print("asha")

"""
#note:

#to access documentation : help(function name,module_name)
#or print(function name or module name .__doc__)
# no of arguments in function defn = no of values in function call ie neither more nor less
#always follows position order,but if we need to break that we can use key=value pair called keyword arguments.
#and first positional arguments and follows later keyword arguments 

"""
"""
x=100
def f1():
    global y #defining y variable as global and it must be mentioned after doc string and should be defined inside a function
    #first we need to create a variable and thn define with value 
    y=20
    print("f1")
    print(f"x is {x}")
    print(f"y is {y}")

def f2():
    global z
    print("f2")
    z=30
    y=22
    print(f"x is {x}")
    print(f"y is {y}")
    print(f"z is {z}")

f1()
f2() #here we get y has not defined as error
print("outside")
print(f"x is {x}")
print(f"y is {y}") #NameError: name 'y' is not defined
print(f"z is {z}")

x=400
f1()
f2()

x=200
print("outside")
print(f"x is {x}")
print(f"y is {y}") #NameError: name 'y' is not defined error
print(f"z is {z}")
#note: values for a variable would be searched from it started to start to program ie towards top

"""


#outside function--global
# inside function-- local
# if we need to change the value inside and outside of function we need to use global keyword
#if we need to change and access the value of variable anywhere in program we need to make it as a global varible.


"""
#global x
x=100 # its global variable by default but what ever variable which is declared inside a function and need t access somewhere in program then we need to make the varaiable as global and use when required

def f1():
    global x #if x isnt a global variable then value defined outside of function is accesed

    x=25
    global y 
    y=20
    print("f1")
    print(f"x is {x}") #inside and global is 25
    print(f"y is {y}")  #20

def f2():
    global z
    print("f2")
    z=30
    y=22
    z=40
    #x=200
    print(f"x is {x}") #200 is no x=200 then global value x=25
    print(f"y is {y}") #22
    print(f"z is {z}") #40

x=400
print(f"x is {x}") #100 as still function f1 isnt called and x isnt defined as global

f1()
f2()

x=200
print("outside")
print(f"x is {x}") #200 due to line 109
print(f"y is {y}") #20
print(f"z is {z}") #40
"""

#function arguments
"""
def display_invoice(name,amount):
    print(f"hi {name}")
    print(f"bill amount is {amount:.2f}")



positional arguments:
display_invoice("sara",20)

keyword arguments:
display_invoice(amount=20,name="sam")

default arguments:
def display_invoice(name,amount=20):
    display_invoice(sara)
    o/p is hi sara
    billamount is default value 20.00

variable-length arguments:


def functionname(formal_arg,*variable_length_arg):
"""
"""
#ex:variable length arguments
def f1(a,b,*c): #8 accepts 0 to n no of values to variable c
    print(a)
    print(b)
    print(c) #(7, 89)
    print(type(c)) #<class 'tuple'>
f1(5,6) # o/p for c is ()
f1(5,6,7,89) # manadatory arguments are for a ,b for rest not compulsoryu to give values and o/p for c is (7,89)
"""

#argument tuple unpacking
#=====================
"""when an argument in function definition is preceded by * asterik,it indicates that argument is taken as a tuple and should be unpacked
when we would accept diffrent inputs at different time,we can use *

but we would need fixed input length we can using variable and define the list and pass the variable as argument
when we need to provide unique values everytime we need to use *
"""
#argument dictionary unpacking
#====================
"""when **(two asterix) is used in function parameters and argument to specificy dictionary packing nd unpacking
"""

def f1(a,b,*c,**args):
    print(a)
    print(b)
    print(c)#tuple format ([40, 560],)
    print(args)# dictionary formT
    print(type(args))
    for k,v in args.items():
        print(k,"=",v)

f1(10,20,[40,560],brand="audi",color="red",milage=100)

#return statement
#==============
#its  last executable statement in function where it returns value to functiona call 
#and also only even though how mnay return we uuse only 1st return return a value later all statements are ignored
#to return a value from a function or module which is executed in other script file and to returned to another script we use return statement

#to return multiple values with multiple return we use generator
"""
def f1(a,b):
    print(a)
    print(b)
    sum=a+b 
    return sum # only this return is performed
    return 100 # this line is never executed
sum=f1(10,20)
print(sum)
"""
 

"""
x=[100]
print(type(x))
y=(10,)
print(type(y))
m=["asha",10,20]
m[0]="siva"
print(m)
student_nmaes=[["a","b","c"],["d",'e','f'],"bob","sam",(10,)]
#student_nmaes[4][0]="asha" #error since we r trying to change tuple values
student_nmaes[4]="asha" #possible to change the value
print(student_nmaes)
"""
if __name__=="__main__":
    f2()

