# 运算符重载
"""
1、运算符重载让类拦截常规的Python运算
2、类可重载所有python表达式运算符
3、类也可重载打印、函数调用、属性点号运算等内置运算
4、重载使类实例的行为像内置类型
5、重载是通过提供特殊名称的类方法来实现的
"""


class Number:
    def __init__(self, data):
        self.data = data

    def __sub__(self, other):
        return self.data - other


# 索引和分片：__getitem__(索引运算) 和__setitem__（索引赋值）
# 如果类中定义或者继承了上述方法，则对于实例的索引运算会自动调用__getitem__
# 索引计算例子
class Indexer:
    def __getitem__(self, item):
        return item ** 2


# 索引分片
class Indexer1:
    data = [5, 6, 7, 8, 9]

    # 当接收分片的时候变为data[slice(2,4,None)]
    def __getitem__(self, item):
        # print("getitem:", item)
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value


if __name__ == "__main__":
    n = Number(8)
    print(n - 2)

    X = Indexer()
    print(X[2])
    # for i in range(5):
    #     print(X[i], end=" ")

    X1 = Indexer1()
    print(X1[0])
    print(X1[2:4])
    X1[2:4] = "hahah"
    # print(X1.data)
    print([i for i in X1])
    