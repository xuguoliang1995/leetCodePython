# 尽管__getattribute__可以捕获比__getattr__更多的属性获取，但是实际上，
# 它们只是 一个主题的不同变体——如果属性没有物理地存储，二者具有相同的效果。
class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):
        # 虚拟的管理属性 如果有未定义的属性就会被拦截
        print("get:", attr)
        return 3


X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print("_" * 40)


class GetAttribute(object):
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    # __getattribute__版本拦截所有的属性获取，并且必须将那些没有管理的属性访问指向 超类获取器以避免循环
    def __getattribute__(self, attr):
        print("get:", attr)
        if attr == "attr3":
            return 3
        else:
            return object.__getattribute__(self, attr)


X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)
