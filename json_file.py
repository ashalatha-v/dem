#json---java script object notation
"""---it is text format for storing and transporting data
-- "self describing and easy to understand"""
#in python json is built in package
"""

python        json
dict          object
list,tuple     array
str           string
int,float     number
True           true
False         false
None           null

1. json string to python dict---json.loads
2. json file to python dict ----> json.load()
3. python dict to json string
4. python dict to json file

"""
#2. json file topython dict ----> json.load()
"""
#file opening syntax

with open('filename.json','mode') as fo:
    ---
    ---

#we cant read json data dirrectly how we read text file

import json

print(dir(json))

with open("user_data.json",'r') as fo:
    k=json.load(fo)
    print(k) 
    print(type(k))
    print(k["name"])
    # while reading the data its not converting json dat to python data
    #for ex in json we have null but in python we have none
    #so while accessing json data using 33 line we r getting json data only
    # so we need to convert to PYTHON DICTIONARY from json data to perform python operations on it

"""

#1. json string to python dict---json.loads()

"""
import json

json_string='{"name":"asha","age":"30","car":null}'
print(type(json_string)) #<class 'str'>
x=json.loads(json_string)
print(x)#{'name': 'asha', 'age': '30', 'car': None}
print(type(x))<class 'dict'>
"""

#4. python dict to json file---- json.dump()
"""import json
person_info={"name":"ashalatha","age":30,"married":True,"car":None}

with open("data.json","w") as fo:
    json.dump(person_info,fo)"""

#3. python dict to json string----json.dumps()
"""
import json
person_info={
    "name":"nyra",
    "age":30,
    "birth_place":"usa",
    "married":True,
    "car":None
}

print(type(person_info)) #<class 'dict'>

json_string=json.dumps(person_info)
print(json_string)
print(type(json_string)) #<class 'str'>

"""


#Data Base:
"""
             #modulename
MySql----    mysql.connector,
sqlite3---- ,#by default we get with python
oracle-----  cx_Oracle
SQL server---pyodbc ,


pip install modulename
"""
"""
       connector
python database script(dbscript.py)--------------------------------      Msql
(import dbmodule
conn(connection object)=dbmodule.connect("username","password","dbname"))
cursor=conn.cursor()   --------------using cursor we execute the commands
cursor.execute("sql query)
cursor.close()
conn.close()


we need to manually stop connection to db if not
ex: if max limit to db connection is 200 if we connect and not disconnect once our work is done...after it reaches 200 limit,others cant connect to db

"""

"""
import sqlite3
conn=sqlite3.connect('test.db')#create db file and connect to it,
print("opened database succesfully ")
conn.execute(''' CREATE TABLE USER
             (ID INT PRIMARY KEY   NOT NULL,
              NAME TEXT  NOT NULL,
              AGE INT  NOT NULL
              );''')
print("table created successfully")
conn.execute("INSERT INTO USER (ID,NAME,AGE) VALUES(1234,'asha',32)")
conn.execute("INSERT INTO USER (ID,NAME,AGE) VALUES(456,'shikha',22)")

conn.commit()
cur=conn.execute("SELECT id,name,age from USER")
#cur variable stores data in tuple format
print(cur)
print(type(cur))
for row in cur:
    print(f"ID:{row[0]}")
    print(f"NAME:{row[1]}")
    print(f"AGE:{row[2]}")
    print("======================")


print("records inserted successfully")
conn.close()
"""

"""
to work with mysql
==================
1. download and install mysql
2. install MySql module(module name mysql.connector) 

how to valiadate
================
got o interactive mode,

import mysql.connector

"""
"""
import mysql.connector
#we need to install mysql-connector-python

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="asha123@",
    database="sakila"

)
mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
print("========================")
#mycursor.execute("CREATE TABLE customers (id INT PRIMARY KEY,name VARCHAR(15),age INT)")
"""
"""mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x) #('category',) o/p ie each table name is treated like a tuple 

print(mycursor.rowcount,"record inseretd successfuly")

mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)

"""
#CRUD OPERATIONS:CREATE,READ,UPDATE,DELETE
"""
import mysql.connector
#we need to install mysql-connector-python

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="asha123@",
    database="sakila"

)
mycursor=mydb.cursor()
sql = "INSERT INTO customers (id,name, age) VALUES (%d,%s, %d)"
val = (1,"John", "21")
mycursor.execute(sql, val)

mydb.commit()
"""

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="asha123@",
    database="sakila"

)
mycursor=mydb.cursor()
"""
#values takes only string as input where inserting into db it checks the type provided inschema
sql = "INSERT INTO customers (id,name,age) VALUES (%s,%s,%s)"
val = [
       ("3","siva","30"),
       ("4","nyra","3"),
       ("5","seysn","5")
]
mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount,"records inserted successfully")
"""

"""sql="DELETE FROM CUSTOMERS WHERE id='5'"
mycursor.execute(sql)
print(mycursor.rowcount,"records deleted")

print("==============")

sql="SELECT * FROM customers"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for r in myresult:
    print(r)

print(mycursor.rowcount,"total records")
"""
sql="UPDATE customers SET name='yamini' WHERE age=3"
mycursor.execute(sql)
mydb.commit()
for i in mycursor:
    print(i)
print(mycursor.rowcount,"total records")










