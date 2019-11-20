# 属性__getattr__ 和__setattr__
"""
__getattr__方法拦截属性点号运算，确切的说，当通过对未定义(不存在)属性和名称
实例进行点号运算时，就会用属性名称作为字符串调用这个方法。如果Python通过继承树的
流程找到这个属性，该方法就不会被调用。
"""


class empty:
    def __getattr__(self, item):
        if item == "age":
            return 40
        else:
            raise AttributeError


"""
__setattr__会拦截所有的赋值语句，如果定义了这个方法，
self.attr = value 就会变为self.__setattr__("attr",value)。
因为在__setattr__对任何self属性做赋值，都会调用__setattr__，导致了
无穷递归循环（最后堆栈出异常）。如果使用这个方法要通过对属性字典做索引运算
来赋值任何实例属性，也就是说是使用self.__dict__["name"] = x 而不是
self.name = x
"""


class accesscontrol:
    def __setattr__(self, key, value):
        if key == "age":
            self.__dict__[key] = value
        else:
            raise AttributeError


if __name__ == "__main__":
    # X = empty()
    # print(X.age)
    # print(X.name)
    C = accesscontrol()
    C.age = 40
    print(C.age)
