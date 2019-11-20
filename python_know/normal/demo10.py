# 类的设计
"""
继承：基于Python中的属性查找的（X.name表达式中）
多态: 在X.method方法中，method的意义取决于X的类型(类)
封装：方法和运算符实现行为，数据隐藏默认是一种惯例。

类可以表示任何用一句话表达的对象和关系，只要用类取代名词，方法取代动词
"""

# 通过通用标记来重载或者不要
"""
通过列表参数重载,以为def只是在类的作用域中把对象赋值给变量名
这个方法函数的最后定义才是唯一保留的。
"""


class C:
    def meth(self, x):
        pass

    def meth(self, x, y, z):
        pass


"""
基于类型的选择，应该把程序代码写成预期的对象接口，而不是特定的数据类型。
"""


class C1:
    def meth(self, *args):
        if len(args) == 1:
            pass
        elif type(args[0]) == int:
            pass


"""

这样可以再更多的类和应用上使用。独特的运算使用独特的方法名称，不要依赖于标记
"""


class C2:
    def meth(self, x):
        x.operation()
