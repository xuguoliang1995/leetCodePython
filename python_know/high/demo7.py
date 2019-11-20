# 字符串知识

"""
1、ASCII标准是美国创建的，定义了从0到127的字符代码，允许每个字符存储在一个8位的字节中(实际上是127位)
2、每个字符一个字节不够，各种符号和重音字符并不在ASCII所定义的可能字符的范围中，所以使用0到255来表示字符
并且把128到255分配给特殊字符，这样的标准叫做Latin-I，广泛使用西欧地区。
3、一些字母表定义了如此多的字符，以至于无法把其中的每一个都表示成一个字节。Unicode考虑到更多的灵活性。
Unicode通常用在国际化的程序中，拥有比8位字符所能表示的更多的字符
4、 UTF-8编码，采用了可变的字节数的方案，小于128的字符代码表示为单个字节，128到0x7ff（2047）之间的代码
转换为两个字节，而每个字节拥有一个128到255之间的值，0x7ff代码转换为3个或者4个字节序列，每个字节序列在
128到255之间。
python2中使用
    （1）str表示8位文本和二进制数据
    （2）unicode用来表示宽字符Unicode文本
python3
     (1)str表示Unicode文本(8位的和更宽的)
    （2）bytes表示二进制数据（不可变不可修改的）
    （3）bytearray 是一种可变的bytes类型。
二进制文件:以为二进制模式打开一个文件的时候，读取数据不会以任何方式解码它，
是直接返回其内容raw并且未经修改。

• str.encode()和bytes(S, encoding)把一个字符串转换为其raw bytes形式，并且
在此过程中根据一个str创建一个bytes。
• bytes.decode()和str(B, encoding)把raw bytes转换为其字符串形式，并且在此
过程中根据一个bytes创建一个str。
字符串格式化只对str有效，对bytes对象无效。
总结：• 对文本数据使用str;
     • 对二进制数据使用bytes;
     • 对想要原处修改的二进制数据使用bytearray。
"""


