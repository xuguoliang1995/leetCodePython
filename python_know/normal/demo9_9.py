# 布尔测试__bool__ __len__
"""

python3首次尝试__bool__来获取一个直接的布尔值，没有的话再使用__len__类
根据对象的长度确定一个真值，


"""


class Truth:
    def __bool__(self): return True

    def __len__(self): return 0


X = Truth()
if X: print("yes")

# 对象的析构函数 __del__
"""

每当实例空间回收的时候（垃圾收集时），析构函数就会自动执行。
"""


class Life:
    def __init__(self, name="ukown"):
        print("hello", name)
        self.name = name

    def __del__(self):
        print("Goodbye", self.name)


brain = Life("brain")
