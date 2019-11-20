class tracer:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 3)
spam(a=4, b=5, c=6)


# 类错误之一：修饰类方法
class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    # 当一个方法名绑定只是绑定到一个简单的函 数，Python向self传递了隐含的主体实例;当它是一个可调用类的实例的时候，就传递 这个类的实例。从技术上讲
    # 当我们用__call__把装饰方法名重绑定到一个类实例对象的时候,python只向self传递了tracer实例;它根本没有在参数列表中传递Person主体。
    @tracer
    def lastName(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
bob.giveRaise(.25)
print(bob.lastName())
