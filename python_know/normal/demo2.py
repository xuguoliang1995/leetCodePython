# 把对象彼此嵌套以组成复合对象，
# 编写Manager扩展的代码，将它嵌入到一个Person中，而不是集成Person

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def lastName(self):
        return self.name.split()[-1]

    def __str__(self):
        return "【Person: %s,%s】" % (self.name, self.pay)


# 替换使用了__getattr__运算符使用重载的方式来做到这点，
# getattr拦截未定义属性的访问，将它委托给嵌入的对象，这里的giveRaise方法依然实现
# 了定制，通过修改快递到嵌入的对象的参数，让Manager变成了控制层，它把调用向下传递到
# 嵌入的对象，而不是向上传递到超类方法。
class Manager:
    def __init__(self, name, pay):
        self.person = Person(name)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)

    # 这里如果属性找不到应该向object向上查找的，使用getattr阻断了，
    # 让它向下查找person指向的类
    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)


if __name__ == "__main__":
    bob = Person("Bob Simith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.1)
    print(sue)
    tom = Manager("Tom Jones", 50000)
    tom.giveRaise(0.1)
    print(tom.lastName())
    print(tom)

    print(bob.__class__.__name__)
    # print(bob.__dict__.keys())
    for key in bob.__dict__:
        print(key, "=>", getattr(bob, key))
