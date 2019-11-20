"""
函数装饰器可以用来管理函数调用和函数对象，类装饰器可以用来管理类实 例和类自身。
通过返回装饰的对象自身而不是一个包装器，装饰器变成了针对函数和类 的一种简单的后创建步骤。


"""


# 每个装饰的函数都会产生一个新的实例来保持状态
class decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        self.func(*args)


# 对拦截简单函数调用有效，但是对类方法函数的时候，并不是有效。
# 当装饰器__call__方法随后运行的时候，其中的self接收装饰器类实例
# 并且类C的实例不会包含到一个*args中，这使得有可能调用分派给最初的方法
class C:
    @decorator
    def medthod(self, x, y):
        pass


def decorator1(cls):
    class wrapper:
        def __init__(self, *args):
            self.wrapper = cls(*args)

        def __getattr__(self, item):
            return getattr(self, item)

    return wrapper


def f1(F):
    return lambda: "X" + F()


def f2(F):
    return lambda: "Y" + F()


def f3(F):
    return lambda: "Z" + F()


@f3
@f2
@f1
def func():
    return "spam"


print(func())  # f3(f2(f1(func)))
