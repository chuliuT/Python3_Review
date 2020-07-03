# >>> import this
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# >>>

# 关键词
import keyword
print(keyword.kwlist)

print("Hello world!")

# 这是注释1
# 这是注释2

'''
多行注释
多行注释
'''

"""
多行注释
多行注释
"""

# 缩进
if True:
    print("True")
else:
    print("False")

# 多行语句  使用 \ 连接
total= 1+ \
    2 + \
    3
print(total)

# [] {} () 多行语句不需要
total=['1','2',
       '3']

str='Hello world'
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次

# 等待用户的输入
# input_sth=input('please input something...')
# print(input_sth)

#同一行多条语句用 分号隔开
import sys; x='Hello'; sys.stdout.write(x+'\n')


#换行
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

# import module
# from xxx import xxx
#from xxx import *
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path