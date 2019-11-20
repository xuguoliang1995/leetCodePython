# 文档字符串
# 文档字符串也可以用于类的部分，他会出现在各种数据结构的顶部的字符串常量
# 有Python在相应的对象的__doc__属性自动保存，他适用于模块文件，函数 定义，以及累和方法

"I am: docstr.__doc__"


def func(args):
    "I am: docstr.func.__doc__"
    pass


class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__"

    def method(self, args):
        "I am: spam.method.__doc__ or self.method.__doc__"
        pass

