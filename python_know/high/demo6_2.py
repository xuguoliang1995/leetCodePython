# 环境管理器
"""
1、计算表达式，所得到的对象称为环境管理器他必须有__enter__和__exit__方法
2、环境管理器__enter__方法调用，如果as字句存在，其返回值会赋值给As子句中变量，否则直接丢弃
3、代码块中嵌套的代码会执行
4、with代码块异常__exit__方法会调用
"""


class TraceBlock:
    def message(self, args):
        print("running", args)

    def __enter__(self):
        print("starting with block")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("exited normal")
        else:
            print("raise an exception", exc_type)
            return False


with TraceBlock() as action:
    action.message("test1")

with TraceBlock() as action:
    action.message("test2")
    raise TypeError
    print("not reached")
