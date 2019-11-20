# 拦截内置操作属性

"""
对于隐式地使用内置操作获取的方法名属 性，这些方法可能根本不会运行。这意味着操作符重载方法调用不能委托给被包装的对象，除非包装类自己重新定义这些方法
在Python 3.0的类中(以及Python 2.6的新式类中)，没有直接的方法来通用 地拦截像打印和加法这样的内置操作。
"""


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)


# 删除Manager中的__str__方法，在Python 3.0下，针对Manager对象，打印不会通过通用的__getattr__拦截器指向 其属性获取。
class Manager1:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)


# 必须在Manager中重新定义__str__来捕获

class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, "mgr", pay)

    def __getattribute__(self, attr):
        person = object.__getattribute__(self, 'person')
        if attr == 'giveRaise':
            return lambda percent: person.giveRaise(percent + .10)
        else:
            return getattr(person, attr)

    def __str__(self):
        person = object.__getattribute__(self, 'person')
        return str(person)


if __name__ == '__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager2('Tom Jones', 50000)
    print(tom.lastName())
    tom.giveRaise(.10)
    print(tom)
