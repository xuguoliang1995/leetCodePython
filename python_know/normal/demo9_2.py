# 多个迭代器
# 当用户用类编写用户定义的迭代器的时候，有我们来决定是支持一个单个还是
# 多个活跃的迭代,要达到多个迭代器的效果，__iter__只需替换迭代器定义新
# 的状态对象，而不是到那会self
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


if __name__ == "__main__":
    alpha = "abcdef"
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I))
    # 每个循环都会获取独立的迭代器独享来记录自己的状态信息，所以每个激活状态的循环都有自己在字符串中的位置
    for x in skipper:
        for y in skipper:
            for j in skipper:
                print(x + y + j, end=" ")




