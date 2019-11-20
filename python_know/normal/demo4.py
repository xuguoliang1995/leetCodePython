# 普通方法实现
class Super:
    def delegate(self):
        self.action()

    def action(self):
        # assert False, "action must be defined"
        raise NotImplementedError("Action must be defined")


# 抽象超类
# 当Provider调用delegate的时候会有两个独立的继承搜索发生：
# 1. 在最初的x.delegate的调用中,python会搜索Provider实例和他上层的对象，
# 知道在Super中找到delegate的方法，实例x会像往常一样传递给这个方法的self参数。
# 2、在Super.delegate方法中，self.action会对self以及它上层的对象启动行的独立继承搜索，
# 因为self指的是Provider实例，在Provider中找到action方法。
# 这种"填空"的代码结构一般就是OOP的软件结构，至少从delegate方法的角度来看，这里例子
# 中的超类有时也被称做超类，也就是类的部分行为默认是由其子类所提供的。如果逾期的方法没有在
# 子类中定义，当继承搜索失败时，Python会引发未定义变量名的异常。

class Provider(Super):
    def action(self):
        print("In Provider.action")


class Sub(Super): pass


"****************************************************************************"
"****************************************************************************"
# 使用装饰器实现
from abc import ABCMeta, abstractmethod


# 带有抽象方法的类是不能继承的（即：我们不能通过调用它来创建一个实例）
# 除非其所有的抽象方法都已经在子类中定义了。
# 缺点是：需要更多的代码
# 优点是：当我们试图产生该类的一个实例的时候，由于没有方法会产生错误，
# 这不会比我们试图调用一个没有的方法更晚，这个功能可以用来定义一个期待的接口，
# 在客户端自动验证
class Super1(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


class Add(Super1): pass


class Add1(Super1):
    def action(self): print("spam")


if __name__ == "__main__":
    # x = Provider()
    # s = Sub()
    # x.delegate()
    # s.delegate()
    # p = Super1()
    X = Add1()
    X.delegate()
