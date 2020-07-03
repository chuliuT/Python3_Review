counter = 100
miles = 100.456
name = 'ethon'
print(counter)
print(miles)
print(name)

# 多变量赋值
a = b = c = 1
a, b, c = 1, 2, 'Hello'

# Python 的数据类型  Number String List Tuple set Dictionary

# 数字
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a),type(b),type(c),type(d))
print(isinstance(a,int))


class A:
    pass

class B(A):
    pass

print(isinstance(A(),A))
print(isinstance(B(),A))
print(type(B())==A)

# 数值运算
print(5+4)
print(4.3-2)
print(3*7)
print(2/4)
print(2//4)
print(17%3)
print(2**5)


# 字符串

str = 'Runoob'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串


# 列表
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

#字符串的反转
def reverse(input):
    inputwords=input.split()
    inputwords=inputwords[-1::-1]
    out=" ".join(inputwords)
    return out

print(reverse('i like python'))

# 元组
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

emptytuple=()
one_element=(1,)

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

# 集合
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素

# 字典
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]= "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
