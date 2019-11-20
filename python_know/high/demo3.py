# __slots__只有在__slots__列表内的这些变量名才可赋值为实例属性。
"""

如果创建了很多实例并且只有几个属性是必须得话，那么每个实例对象分配
一个命名空间字典可能在内存方面代价过于昂贵，要节省空间和执行速度
slot属性可以顺序存储以供快速查找，而不是为每个实例分配一个字典
"""


# 使用slots的时候，实例通常没有一个属性字典，
class C:
    __slots__ = ["a", "b"]


X = C()
X.a = 1
# X.__dict__
setattr(X, "b", 2)


# 没有一个属性命名空间字典不可能给不是slots列表中名称的实例来分配新的名称
class D:
    __slots__ = ["a", "b"]

    def __init__(self):
        self.d = 4


# X1 = D()

# 通过__slots__中包含__dict__仍然可以容纳额外的属性， 两种存储机制
class E:
    __slots__ = ["a", "b", "__dict__"]
    c = 3

    def __init__(self):
        self.d = 4


e = E()
e.a = 1
e.b = 34
print(e.d)
for attr in list(getattr(e, "__dict__", [])) + getattr(e, "__slots__", []):
    print(attr, "=>", getattr(e, attr))



