# 向显示一个类的基本信息


class AttrDisplay:
    # 伪私有类属性，Python自动扩展这样的名称，以包含类的名称，从而使得他们变得真正唯一
    def __gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("%s-%s" % (key, getattr(self, key)))
        return ",".join(attrs)

    def __str__(self):
        return "[%s: %s]" % (self.__class__.__name__, self.__gatherAttrs())




# if __name__ == "__main__":

#     class TopTest(AttrDisplay):
#         count = 0
#
#         def __init__(self):
#             self.attr1 = TopTest.count
#             self.attr2 = TopTest.count + 1
#             TopTest.count += 2
#
#
#     class SubTest(TopTest):
#         # 这里并不会覆盖
#         def gatherAttrs(self):
#             return "haha"
#
#
#     X, Y = TopTest(), SubTest()
#     print(X)
#     print(Y)
