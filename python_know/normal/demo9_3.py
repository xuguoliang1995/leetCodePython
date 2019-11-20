# 成员关系 __contains__
"""
在迭代领域，类通常把in成员关系运算符实现为一个迭代，使用__iter__方法或
__getitem__方法，要支持更加特定的成员关系，类可能编写一个__contains__方法
当出现的时候，该方法由于__iter__方法，__iter__方法优于__getitem__方法
__contains__方法应该把成员关系定义为对一个映射应用建（并且可以快速查找），以及应用
于序列的搜索
"""


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print("get[%s]:" % item, end=" ")

    def __iter__(self):
        print("iter=>", end="")
        self.ix = 0
        return self
    #
    def __next__(self):
        print("next:", end="")
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    # def __contains__(self, item):
    #     print("contains:", end="")
    #     return item in self.data


if __name__ == "__main__":
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end="|")
    # print()
    # print([i * 2 for i in X])
    # print(list(map(bin,X)))
    # I = iter(X)
    # while True:
    #     try:
    #         print(next(I), end="@")
    #     except StopIteration:
    #         break
