list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

L=['Google', 'Runoob', 'Taobao']
print(L[2])
print(L[-2])

squares = [1, 4, 9, 16, 25]
print(squares+[36, 49, 64, 81, 100])