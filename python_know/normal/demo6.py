# 命名字典空间
"""
1、模块的命名空间实际上是以字典的形式来实现的，并且可以由内置属性__dict__显示这一点。
2、类和实例对象也是如此：属性点好运算其实内部就是字典的索引运算。
3、类的继承就是搜索链接的字典而已。
"""


class super:
    def hello(self):
        self.data1 = "spam"


class sub(super):
    def hola(self):
        self.data2 = "eggs"


if __name__ == "__main__":
    X = sub()
    # 当我们只做子类的时候，该子类一开始会有空的命名空间字典，但是有链接会指向它的类，让继承搜索能顺着寻找
    print(X.__dict__)
    # 实例的链接类
    print(X.__class__)
    # sub的超类链接
    print(sub.__bases__)
    # super的超类链接
    print(super.__bases__)
    Y = sub()
    # 当类为属性赋值的时候会填入实例对象，也就是说属性最后位于实例的属性命名空间字典内，
    # 而不是类的。实例对象的命名空间保存了数据，会随实例的不同而不容，self正是进入其命名空间的钩子
    X.hello()
    print(X.__dict__)
    X.hola()
    print(X.__dict__)
    print(sub.__dict__.keys())
    print(super.__dict__.keys())
    print(Y.__dict__)

    # 因为属性时机上是Python的字典值，两种方式可以读取并对其赋值
    # 1、点号运算  2、通过键索引运算
    print(X.data1, X.__dict__["data1"])
    X.data3 = "toast"
    X.__dict__["data4"] = "apple"
    print(X.__dict__)
    # 点号云算可以执行搜索继承，可以存取命名空间字典索引运算无法读取的运算的属性
    print(X.hello())
    # 不能通过继承搜索读取 KeyError: 'hello'
    # print(X.__dict__["hello"])

    # 内置函数dir查看类和实例对象上的情况，这个函数能用在任何带有属性的对象上
    # dir(object)类似于object.__dict__.keys() dir会包含从所有类的隐含超类object类继承的名称"
    print(X.__dict__, Y.__dict__)
    print(list(X.__dict__.keys()))
    print(dir(X))
    print(dir(sub))
    print(dir(super))
