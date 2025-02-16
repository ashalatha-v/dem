import glob
import os
files=glob.glob('*.py')
for i in files:
    print(i)

text_files=glob.glob('*.txt')
for i in text_files:
    os.remove(i)

