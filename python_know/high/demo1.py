# 通过嵌入扩展类型

class Set:
    def __init__(self, value=[]):
        self.data = value
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if x not in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return "Set:" + repr(self.data)


# 通过子类扩展类型
# 改变索引从0开始访问
class Myclass(list):
    def __getitem__(self, item):
        print('(index %s at %s)' % (self, item))
        return list.__getitem__(self, item - 1)


if __name__ == "__main__":
    x = Myclass("abc")
    print(x[1])
