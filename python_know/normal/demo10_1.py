# OOP和继承："是一个"关系，继承是由点号运算启动的，由此出发实例，类以及任何超类中的搜索
# 从设计师的角度，继承是一种定义集合成员的方式，类定义一组内容属性，可由更具体的集合(子类)继承和定制

# OOP和组合："有一个"关系，内嵌对象的集合体，组合类一般都是提供自己的接口，并通过
# 内嵌的对象来实现接口。

# 重访流处理器
"""

这里不是使用简单函数，而是编写类，使用组合机制工作，类提供更强大的结构病支持继承
"""

from abc import ABCMeta, abstractmethod


class Processor(metaclass=ABCMeta):
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while 1:
            data = self.reader.readline()
            if not data: break
            data = self.converte(data)
            self.writer.write()

    @abstractmethod
    def converter(self, data):
        assert False


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()
