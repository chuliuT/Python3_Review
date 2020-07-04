dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

# print("dict['Alice']: ", dict['Alice'])

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
print(dict)

del dict['Name']
dict.clear()
del dict

# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])

