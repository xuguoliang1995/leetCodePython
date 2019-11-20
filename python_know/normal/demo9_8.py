# Call 表达式__call__
"""
当调用实例时使用__call__.如果定义了，Python就会为实例应用函数调用表达式
运行__call__方法，这样可以让类实例的外观和用法类似于函数

"""


class Callee:
    def __call__(self, *args, **kwargs):
        print("Called:", args, kwargs)
class Prod:
    def __init__(self,value):
        self.value = value
    def __call__(self,othre):
        return self.value + othre
class Callback:
    def __init__(self,color):
        self.color = color
    def change(self):
        print("turn", self.color)

if __name__ == "__main__":
    X = Callee()
    X(*[1, 2], **dict(c=3, d=4))
    X(1, *(2,), c=3, **dict(d=4))
