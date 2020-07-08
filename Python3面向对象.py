class Myclass:
    i=12345
    def f(self):
        return  "hello world"

x=Myclass()

print("My class 类的属性方法 i：",x.i)
print(x.f())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5


class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

class people:
    name= ''
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

p=people("runoob",10,30)
p.speak()


# 单继承示例
class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

class speaker():
    topic=''
    name=''
    def __init__(self,n,t):
        self.name=n
        self.topic=t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))

s = student('ken',10,60,3)
s.speak()


class sample(speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test=sample("Tim",25,80,4,"Python")
test.speak()


class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法

class JustCounter:
    __secretCount=0
    publicCount=0

    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print(self.__secretCount)

counter=JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错 私有方法不能访问

# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)