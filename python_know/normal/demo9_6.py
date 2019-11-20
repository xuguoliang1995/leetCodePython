# __repr__和__str__
"""
当类的实例打印或者转化为字符串时__repr__(或其近亲__str__)就会自动
调用。
__repr__用于任何地方，除了定义一个__str__的时候，使用print()和str
的时候。如果没有定义__str__打印还是使用__repr__.
为了确保一个定制显示在所有的环境中都显示，请编写__repr__

"""


class adder:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        self.data += other


class addstr(adder):
    def __str__(self):
        return "[Str:%s]" % self.data

    def __repr__(self):
        return "[repr:%s]" % self.data


X = addstr(4)
print(X)
print((repr(X)))
