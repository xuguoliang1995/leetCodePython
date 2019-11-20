# Python中的类就是一个树结构，一个类继承了好几个类，会从下往上，从左往右查找
# 类的属性和方法
# 定义一个类后类会有自己的命名空间，创建一个实例的时候，实例调用类的方法，然后
# 根据树的查找方法查找到类中的方法，然后赋值的变量会存在实例自己的命名空间。

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


# 好的扩展方式 这里真正想做的是扩展最初的giveRaise，而不是完全替代它，
# 在Python中使用扩展的参数来直接调用其最初的版本
# 实例调用的时候是instance.method(args)
# 使用类调用的时候Python自动转变为class.medthod(instance,args)

class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,"mgr",pay)

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)




# 坏的扩展方式  一旦改变了涨工资的方式，将必须修改两个地方的代码
class Manager1(Person):
    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus))


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
