# 描述符
"""

描述符提供了拦截属性访问的一种替代方法
从技术上讲，property内置函数只是创建一个特 定类型的描述符的一种简化方式，而这种描述符在属性访问时运行方法函数。

"""


# 描述符作为单独的类编写，兵器人针对想要拦截的属性访问操作提供特定命名的访问空间
# 当以相应的方式访问分配给描述符类实例的属性时，描述符类的获取、设置和删除等方法自动运行
class Descriptor:
    # instance参数要么是访问的属性所属的实例(用于instance.attr)，要么当所访问的 属性直接属于类的时候是N o n e(用于c l a s s.a t t r)
    # owner参数，指定了描述符实例要附加到的类
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


"""
带有任何这些方法的类都可以看作是描述符，并且当它们的一个实例分配给另一个类的 属性的时候，
它们的这些方法是特殊的——当访问属性的时候，会自动调用它们。如果 这些方法中的任何一个空缺，
通常意味着不支持相应类型的访问
"""


class Descriptor1(object):
    def __get__(self, instance, owner):
        print(self, instance, owner, sep="\n")

    # 要使得一个属性是只读的,设置__set__抛异常
    def __set__(self, instance, value):
        raise AttributeError("cannot set")


class Subject:
    attr = Descriptor1()


X = Subject()
print(X.attr)
print(Subject.attr)
print(X.__dict__.keys())
# X.attr = 12
