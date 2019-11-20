# 对象的方法: 绑定或无绑定


"""
正常流程：创建一个实例，在单步中调用他的方法，从而打印出传入的参数
其实绑定方法对象是在过程中产生的。
"""


class Spam:
    def doit(self, message):
        print(message)


object1 = Spam()
object1.doit("hello world")

"""
这种方式会传回绑定方法对象，把实例(object1)和方法函数(Spam.doit)打包起来
我们可以把这个绑定方法赋值给另外一个对象名，然后像函数调用
"""
object1 = Spam()
x = object1.doit
x("hello world")

"""
如果对类进行点号运算来获取doit，就会得到无绑定方法对象，也就是函数
对象的引用值，要调用这类方法时，必须传入实例作为最左侧函数

"""
object1 = Spam()
t = Spam.doit
t(object1, "howdy")


class Eggs:
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)


Eggs().m2()
