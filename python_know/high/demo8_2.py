"""
代码定义了一个描述符，来拦截对其客户类中的名为name的一个属性的访问
其方法使用它们的instance参数来访问主题实例中的状态信息，其中指定了实际存储的名称字符串
"""


class Name:
    # self 是Name的实例
    # instance 是Person的类实例
    # ower是Person的类实例
    def __get__(self, instance, owner):
        print("fetch....")
        return instance._name

    def __set__(self, instance, value):
        print("change....")
        instance._name = value

    def __delete__(self, instance):
        print("delete....")
        del instance._name


class Person:
    def __init__(self, name):
        self._name = name

    name = Name()


bob = Person("Bob Smith")
print(bob.name)
bob.name = "Robert Simith"
print(bob.name)
del bob.name

print("_" * 20)
sue = Person("Sue Jones")
print(sue.name)
print(Name.__doc__)

"************************************************************"
"************************************************************"


class Person1:
    def __init__(self, name):
        self._name = name

    class Name:
        def __get__(self, instance, owner):
            print("fetch....")
            return instance._name

        def __set__(self, instance, value):
            print("change....")
            instance._name = value

        def __delete__(self, instance):
            print("delete....")
            del instance._name

    name = Name()


"************************************************************"
"************************************************************"


# 计算属性
class DescSqure:
    def __init__(self, start):
        self.value = start

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value


class Client1:
    X = DescSqure(3)


class Client2:
    X = DescSqure(32)


c1 = Client1()
c2 = Client2()
print(c1.X)
c1.X = 4
print(c1.X)
print(c2.X)

"************************************************************"
"************************************************************"


# 在描述符中使用状态信息
# 描述符会把信息加到自己实例的命名空间
class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print("DescState get")
        return self.value * 10

    def __set__(self, instance, value):
        print("DescState set")
        self.value = value


class CalcAttrs:
    X = DescState(2)
    Y = 3

    def __init__(self):
        self.Z = 4


obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)


class InstState:
    def __get__(self, instance, owner):
        print("InstState get")
        # 这里新的描述符本身没有信息，但是它使用了一个假设存在于实例中的属性—— 这个属性名为_Y，以避免与描述符自身的名称冲突。当这个版本的代码运行的时候，结
        # 果是类似的，但是，管理的是第二个属性，使用位于实例中的状态而不是描述符:

        return instance._Y * 100

    def __set__(self, instance, value):
        print("instance set")
        instance._Y = value


class CalcAtttr1:
    X = DescState(2)
    Y = InstState()

    def __init__(self):
        self._Y = 3
        self.Z = 4


obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)



