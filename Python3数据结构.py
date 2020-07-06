a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2,-1)
print(a)
a.append(333)
print(a)

print(a.index(333))
print(a.reverse(),a)
print(a.sort(),a)

#将列表当做堆栈使用

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
stack.pop()
print(stack)

#将列表当作队列使用
from collections import deque

queue=deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.pop()
print(queue)

#列表推导式
vec=[2,4,6]
print([x*3 for x in vec])
print([[x,x*3] for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([3*x for x in vec if x > 3])

#嵌套列表解析
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]]

print([[row[i] for row in matrix] for i in range(4)])
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

#元组和序列
t = 12345, 54321, 'hello!'
print(t[0],t)
u = t, (1, 2, 3, 4, 5)
print(u)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)

#字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel,tel['jack'])
tel['jack']
print(list(tel.keys()))
print(sorted(tel.keys()))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
