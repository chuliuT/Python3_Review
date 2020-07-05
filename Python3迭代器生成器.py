# list=[1,2,3,4]
# it=iter(list)
# for i in it:
#     print(i)
#
# import sys
#
# list=[1,2,3,4]
# it=iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

class Mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
        else:
            raise StopIteration
        return x


myclass = Mynumber()

myiter = iter(myclass)
for x in myiter:
    print(x)


import sys

def fibonacci(n):
    a,b,c=0,1,0
    while True:
        if (c>n):
            return
        yield a
        a,b=b,a+b
        c+=1
f=fibonacci(10)

while True:
    try:
        print(next(f),end="")
    except StopIteration:
        sys.exit()
