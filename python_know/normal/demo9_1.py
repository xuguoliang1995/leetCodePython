# 迭代器对象：__iter__和__next__
# python中所有的迭代环境都会尝试先用__iter__方法，然后尝试__getitem__
# 从技术角度来讲迭代环境是通过调用内置函数iter去尝试寻找__iter__方法来实现的
# 这种方法应该返回一个迭代器对象，如果已经提供了Python就会重复调用这个迭代器对象的next
# 对象知道发生StopIteration异常，如果没有找到这类__iter__就会改用__getitem__机制
# 定义迭代器类生成平方值
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value * 2


if __name__ == "__main__":
    X = Squares(1,5)

    for i in X:
        print(i, end=" ")
    # __iter__只循环一次
    print([i for i in X])
