# OOP和委托: "包装"对象
"""
委托通常就是指控制器对象内嵌其他对象，而把运算请求传给那些对象
控制器负责管理工作，例如记录存取等。在Python中，委托通常是以
__getattr__钩子方法实现的，因为这个方法会拦截对不存在属性的读取，
因为这个方法会拦截对不存在属性的读取，包装类(有时成为代理类),可以使用
__getattr__把任意读取转发给被包装的对象。包装类包又被包装对象的接口，
而且自己也可以增假其他运算。
"""


class wrapper:
    def __init__(self):
        self.wrapperd = object

    def __getattr__(self, item):
        print("Trace:", item)
        return getattr(self.wrapperd, item)


