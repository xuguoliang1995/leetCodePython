import threading
import time
import functools


# 方法一：使用装饰器
# 使用装饰器实现单例模式
def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return synced_func


def Singleton(cls):
    _instance = {}

    # 线程安全
    @synchronized
    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


# 方法二：使用类 此种方式实现必须通过实例来创建对象。
class Singleton2(object):
    # 使用多线程会出现线程都获得执行权，不能创建多线程的方式。
    # 加锁
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(2)
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        # hassttr判断某个对象是否有某个属性。又返回True
        # getattr 获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
        # 需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
        # 可以在后面添加一对括号。
        # 再加一层判断 如果创建完单例对象后，延时20秒还加锁那么会限制速率。
        if not hasattr(Singleton2, "_instance"):
            with Singleton2._instance_lock:
                if not hasattr(Singleton2, "_instance"):
                    Singleton2._instance = Singleton2(*args, **kwargs)
        return Singleton2._instance


# 第三种方式 基于__new__方法实现。
class Singleton3(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton3, "_instance"):
            with Singleton3._instance_lock:
                if not hasattr(Singleton3, "_instance"):
                    Singleton3._instance = object.__new__(cls)
        return Singleton3._instance


# 第四种方法 基于metaclass元类实现
"""
1.类由type创建，创建类时，type的__init__方法自动执行，
2.类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
3.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
"""


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    # 方法一测试
    # a1 = A(2)
    # a2 = A(3)
    # print(a1.x, a2.x)
    # 方法二的测试
    def task(args):
        obj = Singleton2.instance()
        print(obj)


    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()
    time.sleep(20)
    obj = Singleton2.instance()
    print(obj)
    # 方法3的测试
    # def task(args):
    #     obj = Singleton3()
    #     print(obj)
    # for i in range(10):
    #     t = threading.Thread(target=task, args=[i])
    #     t.start()
    # 方法四测试
    obj1 = Foo('name')
    obj2 = Foo('name')
    print(obj1, obj2)
