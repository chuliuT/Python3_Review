import os
print(os.getcwd())
os.chdir("../")
os.system('mkdir today')

print(dir(os))
help(os)

# import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

import glob
print(glob.glob('*.py'))

import sys
print(sys.argv)

import re

import math
print(math.cos(math.pi/4))

import random

print(random.choice(['apple','pear','banana']))
print(random.sample(range(100),10))

from datetime import date

now=date.today()
print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))


