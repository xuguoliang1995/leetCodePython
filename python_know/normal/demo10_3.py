# 类的伪私有属性
"""

class语句内开头有两个下划线，但结尾没有两个下划线的变量名会自动扩张
从而包含了所在类的名称，例如,像Spam类内__X这样的变量名会自动变成_Spam__X：
原始的变量名会会在头部加入一个下划线，然后是所在类名称。因为修改后的变量名
包含了所在类的名称，变得很独特，不会再同一个层次中其他类所创建的类似变量发生冲突
"""


class C1:
    def meth1(self): self.X = 88

    def meth2(self): print(self.X)


class C2:
    def metha(self): self.X = 99

    def methb(self): print(self.X)


class C3(C1, C2): pass


I = C3()
I.meth1(), I.metha()
print(I.__dict__)


# 使用了伪私有属性
class C1:
    def meth1(self): self.__X = 88

    def meth2(self): print(self.__X)


class C2:
    def metha(self): self.__X = 99

    def methb(self): print(self.__X)


class C3(C1, C2): pass


I = C3()
I.meth1(), I.metha()
print(I.__dict__)


