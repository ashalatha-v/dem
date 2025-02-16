"""class:
it is an blueprint to create an object

object:
it is an instance of class

"""

"""function doesnt need any necessary argument.
function can be directly called without any object.
function are defined outside the class. 

def f1():
    pass
f1()
#built

method needs only necessary argument where it can be named as any name.
usually we use self as default argument.
method can be called only using a object created.
methods are defined inside the class.

objectname.methodname()


class x:
    def m1(): #it we dont provide one argument which usually used is self 
#it gives TypeError: x.m1() takes 0 positional arguments but 1 was given
        print("m1")        
x1=x()
print(x1)
#for x1 object is created by assigning a value to it so while
#calling x1.m() it takes object address by default internally so in order to hold that we need an argument in a method everytime to accept the object reference address so it gives error if not self as default argument 
# in method
#  

x1.m1()
"""
"""
class x:
    def m1(self):  #self or any name is manadte to hold object address
        print("m1")  
        print(self)    #self value of object(it can be x1 object)  
x1=x() # now x1 object is craeted using a reference value or address 
#which is passed to x1.m1() so we need to provide a argument to hold address passed internally so if not given we get error

x1.m1()"""
"""
Class varibales: 
1. static variables
2.non sttatic or instance variables
3. local variables
"""

"""
static variables:vardiables which are defined inside class and outside of all methods
-- static variables,we can call with classname or object name
ie,classname.static_variable
"""
"""
class x:
    k=20
    def m(self):
        i=100
        print(f" in m, value of i is {i}")
        print("im in m")
        print(x.k)  #we can access here using classname.static_variable
    def m1(self):
        print("im in m1")
        print(x.k)
        #print(f"In m1,value of i is {i}") #error
x1=x()
print(x.k)# here we can access using classname.static_variable or
print(x1.k) # object_name.static_variable
x1.m()
x1.m1()
#print(f"val of i is {i}") #error as i value can be only accesed with m 
"""
"""local variables:variables defined inside method 
local variables we can access only within specific method
"""
"""
non -static variables(instance variables):
we can define only inside a method or inside a constructor using below
(deafult argument in method(self).variablename)
--- if we use self.variablename while defining we can access in other methods inside a class too

not recommended to define instance variable in a method because

"""
"""
class x:
    def insert(self):
        print("in insert)")
        self.a="100"
        self.b="200"
        print(self.a)
        print(self.b)
    def display(self):
        print("in display method")
        print(self.a)
        print(self.b)
    def modify(self):
        self.a=self.a+"10"
        self.b=self.b+"20"

x1=x()
x1.display() # problem is calling directly display method results error below one

# print(self.a)
# AttributeError: 'x' object has no attribute 'a'
#error is because  a and b values are initialised at insert method.so if we call insert method then a and b values are initialised then a and b values are printed
#so not best pratice is because display has dependency on insert method for initializing
#  so
x1=x()
#x1.display()#AttributeError: 'x' object has no attribute 'a'
x1.modify()#AttributeError: 'x' object has no attribute 'a'
"""
"""x1=x()
x1.insert() #if this process then no problem as we r calling insert for initialising the values using self.a and self .b
x1.display()
x1.modify()"""

#best to use instant varibales in constructor

"""constructor:
--is special method and constructor name should always be __init__(self)
-- used to define and initialise non static variable



class x:
    def __init__(self):
        print("constructor of x")
        self.a=100
    def m1(self):
        print("im in m1")

x1=x() #1 object 1 constructor is executed
x1.m1()# but using 1 object we can call method multiple times.
x1.m1()      
x2=x()
print(x2.a) #using object x2 we need to cal a value initialised in constructor


#parameterised contsructor:
class x:
    def __init__(self,a):
        print("constructor of x")
        self.a=a
        print(self.a)
    def m1(self):
        print("im in m1")

x1=x(10) #10 is for a value  )
x1.m1()
x1.m1()      
x2=x(100)
print(x2.a)
"""
"""
class BankApp:
    Bank_name="HDFC"
    def __init__(self,customer_name,cust_accnumber,customer_accbal,cust_address):
        self.customer_name=customer_name
        self.cust_accnumber=cust_accnumber
        self.customer_accbal=customer_accbal
        self.cust_address=cust_address

    def deposit(self,deposit_amount):
        self.customer_accbal=self.customer_accbal+deposit_amount
    def withdraw(self,withdraw_amount):
        if self.customer_accbal>withdraw_amount:
            self.customer_accbal=self.customer_accbal-withdraw_amount
        else:
            print(f"insufficient balanace, available balance is {self.customer_accbal}")
    def balance_enquiry(self):
        print(f"hi {self.customer_name} your acc balance is {self.customer_accbal}")
    def display(self):
        print("\n#####customer info#####")
        print(f"your name is:{self.customer_name}")
        print(f"your account number is is:{self.cust_accnumber}")
        print(f"your available balance  is:{self.customer_accbal}")
        print(f"your bank name :{BankApp.Bank_name}")

cust1=BankApp('siri',1001,1000,'usa')

cust1.balance_enquiry()
cust1.deposit(2000)
cust1.withdraw(15500)
cust1.balance_enquiry()
cust1.display()

cust1=BankApp('nyra',10001,2000,'india')
cust1.balance_enquiry()
cust1.deposit(2000)
cust1.withdraw(5500)
cust1.balance_enquiry()
cust1.display()
"""


#inheritance:inheriting one parent class propeties from one child class 
"""
class x: #parent class or super class
    def m1(self):
        print("in x of m1")
class y(x):#child or dervied or sub class
    def m2(self):
        print("in y of m2")

y1=y()
y1.m2()
y1.m1() #x1=x() x1.m1() no ned as inheritance is applied
#x1=x() x1.m1()

"""
#types of inheritance:
"""
simple inheritance (one parent one child)
,multiple inheritance (multiple parent(p1,p2,...pn)--- single child),
multi level inheritance( granparent-- parent--child),
hierachical inheritance( single parent --> multi child( child 1 child2)),
hybrid inheritance( combination of any two inheritance)

"""
#multiple inheritance

"""class parentclass1:
    def feature1(self):
        print("feature1 in parentclass1")

class parentclass2:
    def feature2(self):
        print("feature2 of parent2")

class childclass(parentclass1,parentclass2):
    def feature3(self):
        print("feature3 of childclass")

c=childclass()
c.feature1()
c.feature2()
c.feature3()
"""

#multilevel inheritance:
"""
class grandparent():
    def feature1(self):
        print("feature1 of grandparent")

class parent(grandparent):
    def feature2(self):
        print("feature2 of parent")

class child(parent):
    def feature3():
        print("feature3 of child")

p=parent()
p.feature2()
p.feature1()
p.feature3()#error since we have created object for parent class not child class so we cant access feature3
#AttributeError: 'parent' object has no attribute 'feature3'. Did you mean: 'feature1'?

c=child()
c.feature1()
c.feature2()
c.feature3()
"""

#hierachical inheritance:
"""
class parentclass1:
    def feature1(self):
        print("feature of parentclass1")

class childclass1(parentclass1):
    def feature2(self):
        print("feature of childclass1")

class childclass2(parentclass1):
    def feature3(self):
        print("feature3 of childclass2")

c1=childclass1()
c1.feature2()
c1.feature1()

c2=childclass2()
c2.feature3()
c2.feature1()

"""
#hybrid inheritance:combination of any 2 inheritances
"""
class parentclass():
    def feature1(self):
        print("feature1 of parentclass")
class childclass1(parentclass):
    def feature2(self):
        print("feature2 of child class1")
class childclass2(parentclass):
    def feature3(self):
        print("feature3 of childclass2")
class childclass(childclass1,childclass2):
    def feature4(self):
        print("feature4 of childclass")
c=childclass()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
"""

#polymorphism(poly:many and morph:forms):
"""same function name but different signatures being used for different types
       
#+-- addition +-- conatenation
#*--multiplication and  string repitation
types of polymorphism:
1. method overloading same method name different no of arguments
2. method overriding

"""
#1. method overloading:
"""within same class multiple methods with same name with different no of arguments is called method overloading

class x:
    def m1(self,a,b):
        self.a=a
        self.b=b
        print("m1 with a and b")
        print(f"a={self.a},b={self.b}")

    def m1(self):
        print("m1")
    def m1(self,a):
        self.a=a
        print("m1 with a")
        print(self.a)

x1=x()
x1.m1(20,30) 
x1.m1()
x1.m1(10)
"""
#evrytime last method ie def m1(self,a) is considered and checks for any method method calling
#TypeError: x.m1() takes 2 positional arguments but 3 were given for line 343

"""PYTHON DOESNT SUPPORT METHOD OVERLOADING"""

#2. method overriding:super() keyword or using classname.methodname()
"""
class x:
    def m1(self):
        print("in m1 of")

class y(x):
    def m1(self):
        super().m1()
        print("###########")
        x.m1()
        print("################")
        print("m1 of y")

y1=y()
y1.m1() 
#when parent class has same method as that of child class as object y1 is created for child class,method will be searched first in child class
#  by default child class method is called so to call parent class we need to use super().
"""
#constructor overriding()(    super().__init__()     ):
"""
class x:
    def __init__(self):
        self.value="inside parent"
    def show(self):
        print(self.value)

class y(x):
    def __init__(self):
        super().__init__()
        self.value="inside child"
    def show(self):
        print(self.value)

x1=x()
x1.show()

y1=y()
#if we want to call x class show() method from child class then we need to give y(x) and inside init child method super().__init__() then we can access parent init method from child method
#    
y1.show()
"""

#abstraction:restriction of data members,variabes etc 
#python access modifiers:
# types: 
# public:default-- self.name--can access evrywhere,
# protected:_(single underscore)--self._name ----in others packages we cant access,
# private:__(two underscore)--self.__name ------we can access only in same class
"""
class person:
    def __init__(self,name,age,height):
        self.name=name #public
        self._age= age #protected
        self.__height=height #private
    #def show(self):
     #   print(self.__height)

p1=person("john",30,170)

print(p1.name)
print(p1._age)
#p1.show()
#print(p1.__height) #AttributeError: 'person' object has no attribute '__height' AS IT IS ctreated as private

#another way to access private variable outside class we can use below
print(dir(p1))  # '_person__height', 'name', 'show'
print(p1._person__height) # _classname__propertyname

"""

#advanced/functional programming:
"""
--lamda expressions
--map()
--filter()

more efficient way to write and expert level programmers uses these concept
"""


#exceptional handling:
"""
1. compilation or syntax error( human error--- syntax error,indentationerror,taberror)

until synatx error are cleared it wont proceed with executing the program

2. run time error()----
ex:
name error
filenotfounderror
indexc error
value error
dividebyzeroerror 
when eversuch exception comes instead of abnormally terminating the execution where we need to provide some user understandable o/p regarding the error with print statements


where above need to be handled using exception handling
"""

#print(dir(__builtins__)) #to get list of builtin error


#1.try and except wth multiple except
"""
print("hi")
x=int(input("enter first number"))
y=int(input("enter second number:"))
try:
    result=x/y
    print(result)
except ZeroDivisionError:
    print("denominator value shouldnt be zero")
except:
    print("something went wrong")
print("bye")
"""
#2. try and multiple except block 
#3. try and except and finally

"""connection related issues we can solve suing finally block
for ex we a connected to db but due to some error cursor object and connection object wont close
so in order to happen them we put them in finally block

try:
    -----
    ------
    -----
except:
    ----
    ---
    ----
finally:
    -----
    ----

whether try block executes correctly or not and whetehr except block executes or not 
finally block will get executed irrespective of try and except execution
statements which needs to be executed at any cost should be specified in finally block.


fo=None
try:
    fo=open('test100.txt','r')
    for i in fo:
        print(i)
except FileNotFoundError:
    print("something went error")
    print(a)
print(fo)
fo.close()
usually when something goes wrong in try block except handles and executes rest of code
but when except block has error then rest of code wont be executed
so inorder to definetely execute some code when try or except is executed or not we put that in finally block

NameError: name 'a' is not defined  """
"""fo=None
try:
    fo=open('test.txt','r')
    for i in fo:
        print(i)
except FileNotFoundError:
    print("something went error")
    print(a)
except:
    print("something went wrong")
finally:
    print(fo)
    #if file doesnot exist then we cant close right so if condition
    if fo!=None:
        fo.close()
"""
"""
try:
    stmt-1
    stmt2
    stmt3
    try:
        stm4
        stmt5
        stmt6
    except xy:
        stmt7
    finally:
        stmt8
    stmt9
except yx:
    stmt10
finally:
    stmt11
stmt12

case 6:
if stmt 5 raised error and corresponding inner block not matched but outer except block not matches
(stmt 1,2,3,4,8,11) abnormal excecution

case 5:
if stmt 5 raised error and corresponding inner block not matched but outer except block matches
(stmt 1,2,3,4,8,10,11,12) normal termination 

case4:
if stmt 5 raising error, and inner except block is matched 
(stmt 1,2,3,4,7,8,9,11,12 )normal termination

case3:
if exception raised at stmt2 and corresponding except block not matched
stmt1,11 error occurs abnormal termination

case2:
if exception raised at stmt2 and corresponding except block matched
(stmt1,10,11,12) normal termination

case1:
if no exception,then except stmt7 and stmt10 everything will be executed one by one
(stmt 1,2,3,4,5,6,8,9,11,12)

case 2:


"""
#4. user defined exceptions:we create our own exception
#raise keyword is used to create an user defined exception
#raise-- it is used to raise an exception and stop the further execution

"""age=int(input("enter age:"))
if type(age) is not int:
    raise TypeError("only int values accepted")

name=input("enter name")
age=int(input("enter age"))
print(f" your name is:{name}")

if age <= 0:
    raise Exception("sorry number 0 and below 0 isnt accepted")
else:
    print(f"age is:{age}")
    """

#set:
"""
---similar to list 
--- it is a collection type variable.
--- collection of any data type items and represented using {} with coma seperated items.
---uniques values no dulplicate values
---it never print in same order
---unordered,non duplicate,un-indexed,set is mutable,iterable,
---indexing is not possible as o/p is not same everytime
---traversing possible

x={10,20,"asha",40,30,50,50,40}
print(x) 
#o/p:{50, 20, 'asha',40, 10, 30}
print(dir(set))

x=[10,20,30,40,10,50,60]
s=set(x)
l=list(s)
print(s)
print(l) #list created ealier and now is different as its cpnverted to set in middle
for i in s:
    print(i)
    
x={10,20,30,40,10,50,60}
print(id(x)) # 2230197901952
x.add('asha') #add method to add element to a set
print(id(x)) #2230197901952 
#as even after adding the elements to a set refernec or address hasnt changed we say set is mutable 

"""
#set methods
# print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 
# 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
# 'issuperset', 'pop', 'remove', 'symmetric_difference', 
# 'symmetric_difference_update', 'union', 'update']

"""
add()--- to add a new value to set
clear()---to clear the values in set
copy()--- copy the values but not reference where copy of have different reference

x={10,20,30,40}
x1=x.clear()
print(x1) #None

x={10,20,30,40,'asha','siva'}
x1=x
print(x)
print(x1)
print("############")
print(id(x))
print(id(x1))
x.add('nyra') #nyra is added to both x and x1 as we have used = to copy values
print("####")
print(x)
print(x1)


"""
"""
#union():
x={10,20,40,50}
y={50,70,100,200}
unionres=x.union(y)
print(unionres)

#intersection()
x={10,20,30,50,70,80}
y={20,30,40,60,70,80}
interx=x.intersection(y)
print(interx) #{80, 20, 70, 30}
print(x)#{80, 50, 20, 70, 10, 30}

#intersection_update():trying to update in original object
print("######")
x.intersection_update(y)
print(x)#{80, 20, 70, 30}

#difference()
x={10,20,30,50,70,80}
y={20,30,40,60,70,80}
diffx=x.difference(y) #wont reflect in x variable
diffy=y.difference(x)
print(diffx) #{50, 10} apart from common values in both rest of values in x is printed

#difference_update(): trying to update in original object
x={10,20,30,50,70,80}
y={20,30,40,60,70,80}
print(x)
x.difference_update(y) #out of difference is update in x
print("#########")
print(x) #{50, 10}

#method starting with is results in boolean value

#issubset():
x={10,20,30,40}
y={20,30,40}
#since all values of y present in x so x is superset and y= subset

print(y.issubset(x)) #true
print(x.issubset(y)) #false
print(x.issuperset(y)) #true


#pop()--- deletes random Value 
x={10,20,40,50}
print(x)
x.pop()
print(x)

#remove()---remove specific value
x={10,20,30,40}
x.remove(20)
print(x) #{10,30,40}

#symmetric_difference()--x.difference(y) and y.difference(x) is checked
x={10,20,30,40,50}
y={60,70,80,10,20}
print(x.difference(y))
print(y.difference(x))
print(x.symmetric_difference(y)) 
print(x) #contains original items
print(x.symmetric_difference_update(y))
print(x) #now x values is updated with symmetric difference update

#update()-- to add multiple values to a set

x={10,20,30,'asha','siva'}
y={'nyra',10,'asha'}
x.update(y) 
print(x)#{'nyra', 20, 'siva', 10, 30, 'asha'}

#remove() and discard() -does same remove the object but
#  if we use remove() and if value is in set it removes else it gives key error
# if we use discard () and if value is in set it discards else it ignores it( no error if values not exists)

 
x={10,20,'asha','nyra',40}
y={10,20,'asha','nyra',40}
x.remove(20)
print(x)
print("##########")
y.discard('asha')
print(y)
"""