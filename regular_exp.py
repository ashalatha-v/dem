r"""import re
with open('sample.txt')as fo:
    for i in fo:
        if re.search(r'[a-zA-Z0-9]+\s[a-zA-Z0-9]+\s[a-zA-Z0-9]+',i):# prints 3 or more words but not below 3 words in a line
                print(i,end="")

        if re.search(r'\w+\s\w+\s\w+',i):# prints 3 or more words but not below 3 words in a line
            print(i,end="")

        if re.search('[0-9]{10}',i): #or \d{10} to search 10 digit phone number
            print(i,end="")
   
        #to match only 4 letter word
        if re.search('[a-z]{4}',i):# or [a-zA-Z]{4}
            print(i,end="")
            
        if re.search(r'\w+[@]\w+[.]\w+',i):
            print(i,end="")
            
        if re.search('nyra|siva',i):
            print(i,end="")

"""
#name validation:
r"""
name should be alphabet
name should contains min of 2 characters

[a-zA-z]{2,}
r"""
#mobile number validation
"""---number should start with 6 or 7 or 8 or 9
--- number should be of 10digit number
[6-9][0-9]{9}
"""

#how to search and display valid emaid in a file / 

#[a-zA-Z0-9]{10,} or \w+  ----- to match name minimum of 10 chars
r"""\w+[@][a-zA-Z]+[.][a-zA-Z]+""" #or \w+[@]\w+[.]\w+
r""" if we give . directly after \w it will consider it as to accept single charcter
so best practice is to give inside [.] 
"""

#word pattern
""" \b is boundary
start and end with same word \bword\b
starts with \bword
ends with word\b

\s--- for new line,tab sapce,space
\b --it identifies word is starting and when space occurs it thinks word ended  
"""

#line pattern
"""
line start with ^word ex: ^python
line ends with word$  ex: python $

to search if a line contain only word python then use
^python$

line starts with python and end with python
^python[a-zA-Z0-9]*python$  or ^python.*python$ 

^[python]--means line starts with p or y or t or h or o or n
^[^python]---means it accepts lines not starting with p or y or t or h or o or n


"""
import re
with open('sample.txt','r') as fo:
    r"""
    for i in fo:
        if re.search('^python',i):
            print(i,end="")
    print("#############")       
    for j in fo:
        if re.search('python$',j):
            print(i,end="")
            
    print("#############")        
    for k in fo:
        if re.search('^python$',k):
            print(i,end="")
    print("#############")

    for i in fo:
        #if re.search('^python.*python$',i):
        #if re.search('^[^[0-9][python]]',i):
        #if re.search(r'\bpython\b',i): #to consider \b as raw meaning don consider as b
        #if re.search(r'\bpython',i): # checks for a word starts with python but not consider about end word
        if re.search(r'python\b',i): 
            print(i,end="")     


student_name="ravi ramu bob sameer siri"
prog_loist="perl python ruby shell java"

#pattern object=to apply a pattern to any input we deine in a pattern word


import re

#pattern=re.compile("\w{4}") 
pattern=re.compile(r"\b\w{4}\b") 

print(pattern)
k= pattern.findall(student_name)
print(k) #here output is ['ravi', 'ramu', 'same', 'siri'] ie for sameer whoch is not be prrsent at output its printing 4 word from sameer so need to sesrch as a word

l=pattern.findall(prog_loist)
print(l)
"""

import re
with open('sample.txt')as fo:
    for i in fo:    
        #if re.search(r'\w+\s\w+\s\w+',i):
        if re.search(r'^\w+\s\w+\s\w+$',i):
            print(i,end="")
#it prints where line contains 3 words as in 4 words in aline also it prints that too as it contains 3 words in it
#so if we need to print a line which has 3 words we need to use line pattern ie from end starting to end we need 3 words onlt
# so use ^ at start and $ at end ie  