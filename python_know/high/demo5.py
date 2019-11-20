# 静态方法和显式类名称可能对于处理一个类本地的数据来说可能是更好地方法'
# 类方法可能更适合处理对层级中的每个类不同的数据

# 静态方法统计实例
class SpamStatic:
    numInstance = 0

    def __init__(self):
        SpamStatic.numInstance += 1

    def printNumInstance():
        print(SpamStatic.numInstance)

    printNumInstance = staticmethod(printNumInstance)


# 类方法统计实例
class Spam:
    numInstance = 0

    def count(cls):
        cls.numInstance += 1

    def __init__(self):
        self.count()

    count = classmethod(count)


class Sub(Spam):
    numInstance = 0

    def __init__(self):
        Spam.__init__(self)


class Other(Spam):
    numInstance = 0


x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3 = Other(), Other(), Other()
print(x.numInstance, y1.numInstance, z1.numInstance)
