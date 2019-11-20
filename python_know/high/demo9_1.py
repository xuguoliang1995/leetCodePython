# 跟踪调用
# 类装饰计数器
class tracer:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)


# 类实例属性来显式地保存状态。包装的函数和调用计数器都是针对每个实例的信息——每个装饰都有自己的拷贝
spam(1, 2, 3)  # calls = 1
spam("a", "b", "c")  # calls = 2
eggs(1, 2)  # calls = 1
eggs(3, 4)  # calls = 2

print("**" * 40)

# 封闭作用域和全局作用域
calls = 0


def tracer1(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


@tracer1
def spam(a, b, c):
    print(a + b + c)


@tracer1
def eggs(x, y):
    print(x ** y)


# 和类实例属性不同，全局计数器是跨程序的，而不是针对每个 函数的——对于任何跟踪的函数调用，计数器都会递增
spam(1, 2, 3)  # calls = 1
spam("a", "b", "c")  # calls = 2
eggs(1, 2)  # calls = 3
eggs(3, 4)  # calls = 4
print("**" * 40)


def tracer2(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)

    return wrapper


# 注意，这种方法有效，只是因为名称wrapper保持在封闭的tracer函数的作用域中。
# 当我们随后增加wrapper.calls时，并不是在修改名称wrapper本身，因此，不需要nonlocal声明。
def tracer3(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print("call %s to %s" % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper
