# 管理技术的比较
"""
注意
def __getattribute__(self, name):
    x = object.__getattribute__(self, 'other')
def __setattr__(self, name, value):
     self.__dict__['other'] = value
def __setattr__(self, name, value):
     object.__setattr__(self, 'other', value)
"""


# property描述符实现
class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def getSuqre(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value

    square = property(getSuqre, setSquare)

    def getCube(self):
        return self._cube ** 3

    cube = property(getCube)


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)

print("*" * 40)


# 描述符实现，描述符把基础值存储为实例状态，因此，它们必须再次使用下划线开头，以便不会与描述符的名称冲突
class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2

    def __set__(self, instance, value):
        instance._square = value


class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3


class Powers1:
    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


X = Powers1(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)
print("*" * 40)


# 使用__getattr__和__setattr__
class Powers2:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, name):
        if name == "square":
            return self._square ** 2
        elif name == "cube":
            return self._cube ** 3
        else:
            raise TypeError

    # 对被管理的名称访问是未定义的，并且由此调用我们的方法。我们还需要编写 一个__setattrr__来拦截赋值，并且注意避免其潜在的循环:
    def __setattr__(self, name, value):
        if name == "square":
            self.__dict__["_square"] = value
        else:
            self.__dict__[name] = value


X = Powers2(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)
print("*" * 40)


class Powers3:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
        if name == "square":
            return object.__getattribute__(self, "_square") ** 2
        elif name == "cube":
            return object.__getattribute__(self, "_cube") ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "square":
            self.__dict__["_square"] = value
        else:
            self.__dict__[name] = value


X = Powers3(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)



