basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

thisset.update({1,3})
print(thisset)

thisset.remove('Taobao')
print(thisset)
thisset.discard('Taobao')
print(thisset)