# __getattr__和__getattribute__

"""
属性获取拦截表现的两种形式：
1、__getattr__针对未定义的属性运行，也就是说，属性没有运行在实例上，或者没有从其类继承
2、__getattribute__针对每个属性，使用它的时候，必须小心避免通过把属性访问
传递给超类而导致递归循环


"""


def __getattr__(self, name): pass  # On undefined attribute getch


def __getattribute__(self, name): pass  # On all arribute fetch


def __setattr__(self, name, value): pass  # On all atrribute assignment


def __delattr__(self, name): pass  # On all attriubte deletion


# 特性和描述符没有这样的类似功能，做不到对每个可能的包装对象中每个可能的属性编 写访问器。
class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        return getattr(self.wrapped, item)


# 避免属性拦截中的循环 在一个__getattribute_方法代码内部的另一次属性获取，
# 将会再次触发 __getattribute__，并且代码将会循环直到内存耗尽
def __getattribute__(self, name):
    x = self.other


# 解决方法把获取执行一个更高的类，而不是跳过这个版本
def __getattribute__(self, name):
    x = object.__getattribute__(self, "other")


# 对于__setattr__，情况是类似的。在这个方法内赋值任何属性，都会再次触发 __setattr__并创建一个类似的循环
def __setattr__(self, name, value):
    self.other = name


# 要解决这个问题，把属性作为实例的__d i c t__命名空间字典中的一个键赋值。这样就避 免了直接的属性赋值:
def __setattr__(self, name, value):
    self.__dict__["other"] = value


# 尽管这种方法比较少用到，但__setattr__也可以把自己的属性赋值传递给一个更高的超 类而避免循环，就像__getattribute__一样:
def __setattr__(self, name, value):
    object.__setattr__(self, 'other', value)


class Person:
    def __init__(self, name):
        self._name = name

    # 方法1
    # def __getattr__(self, item):
    #     if item == "name":
    #         print("fetch")
    #         return self._name
    #     else:
    #         raise AttributeError

    # 方法2：
    def __getattribute__(self, item):
        if item == "name":
            print("fetch...")
            item = "_name"
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "name":
            print("change....")
            key = "_name"
        self.__dict__[key] = value

    def __delattr__(self, item):
        if item == "name":
            print("remove...")
            item = "_name"
        del self.__dict__[item]


bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name
print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)  # print(Person.name.__doc__)


class AttrSqure:
    def __init__(self, start):
        self.value = start

    # def __getattr__(self, item):
    #     if item == "X":
    #         return self.value ** 2
    #     else:
    #         raise AttributeError

    """
    • 构造函数中的self.value=start 触发__setattr__。
    • __getattribute__中self.value再次触发__getattribute__。
    
    """

    def __getattribute__(self, item):
        if item == "X":
            return self.value ** 2
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "X":
            attr = value
        self.__dict__[key] = value


A = AttrSqure(3)
B = AttrSqure(32)
A.X = 4
print(A.X)
print(B.X)


class getItem:
    def __getitem__(self, item):
        print("hahahha", item)
        return self.data[item]


X = getItem()
X.data = "spam"
