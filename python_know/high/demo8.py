# 属性管理器
"""
__getattr__和__setattr__方法，吧未定义的属性获取的所有的属性赋值指向通用的处理器方法
__getattribute__方法，把所有属性获取都指向所有类中的一个泛型处理器
property内置函数,把特定属性访问定位到get和set处理器方法的类的实例。
property特性协议允许我们把一个特定属性的get和set操作指向我们所提供的函数或方法，使得我 们能够插入在属性访问的时候自动运行的代码，拦截属性删除

"""


# 第一种方法的写法

class Person1:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    name = property(fget=getName, fset=setName, fdel=delName, doc="name")


# ************************************************************************
# 继承类的写法
class Super:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    name = property(fget=getName, fset=setName, fdel=delName, doc="name")


class Person2(Super):
    pass


# ************************************************************************
# 装饰器的写法
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        "name property docs"
        print("fetch....")
        return self._name

    @name.setter
    def name(self, value):
        print("change...")
        self._name = value

    @name.deleter
    def name(self):
        print("remove")
        del self._name


if __name__ == "__main__":
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    del bob.name
    print('-' * 20)
    sue = Person('Sue Jones')
    print(sue.name)
    print(Person.name.__doc__)
