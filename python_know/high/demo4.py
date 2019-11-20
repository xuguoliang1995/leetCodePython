# 类特性
"""
另外一种方式让新式类定义自动调用的方法，来读取或者赋值实例属性
这种只是在读取所需要的动态计算变量名时才会发生额外的发放调用
特性的产生是以（获得、设置以及删除运算的处理器）以及通过文档字符串调用
内置函数property

"""


# 改用特性来写,运行起来更快，输入的代码更少，对我们不希望进行动态计算的属性进行赋值时不会发生额外的方法调用

class newprops(object):
    def getage(self):
        return 40

    def setage(self, value):
        self._age = value

    age = property(getage, setage, None, "")


n = newprops()
print(n.age)



# 等效的经典类可能会引起额外的方法调用，而且需要通过属性字典传递属性赋值语句
# 以避免死循环（或者对于新式类来说回导向object超类的__setattr__）
# 大多数情况下，编写类时，要支持的属性集无法确认，甚至无法以任何具体形式存在（例如
# 委托任意方法的引用给被包装/嵌入对象时）
class classic:
    def __getattr__(self, item):
        if item == "age":
            return 40
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        print("set:", key, value)
        if key == "age":
            self.__dict__["_age"] = value
        else:
            self.__dict__["name"] = value


x = classic()
x.age = 10

# x.name









