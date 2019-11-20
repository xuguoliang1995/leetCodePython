# 命令空间
"""
点号和无点号的变量名会有不同的处理方式，而有些作用域是用于对对象命令空间做初始化设定的
1、无点号运算的变量名（例如：X）与作用域相对应
2、点号的属性名（例如：object.X）使用的是对象的命令空间
3、有些作用域会对对象的命令空间进行初始化（模块和类）



"""
# 模块的属性
X = 11


def f():
    print(X)


def g():
    # 函数内的本地变量
    X = 22
    print(X)


class C:
    # 类属性
    X = 33

    def m(self):
        # 方法中的本地变量
        X = 44
        # 实例属性
        self.X = 55


if __name__ == "__main__":
    """
    简单变量名：如果赋值就不是全局变量
    无点号的简单变量名函数的的查找顺序，LEGB
    赋值语句（X = value）
       使变量名成为本地变量：在当前作用域内，创建或改变变量名X，除非声明他是全局变量
    引用(X)
       在当前作用内搜索变量名X，之后实在任何以及所有的嵌套函数中，然后实在当前的全局作用域中搜索
       最后实在内置作用域中
    Local 局部名字的最内层（innermost）作用域，如函数/方法/类的内部局部作用域；
  　 Enclosing：根据嵌套层次从内到外搜索，包含非局部（nonlocal）非全局（nonglobal）名字的任意封闭函数的作用域。如两个嵌套的函数，内层函数的作用域是局部作用域，外层函数作用域就是内层函数的 Enclosing作用域；
  　 Global：倒数第二次被搜索，包含当前模块全局名字的作用域；
　　 Built-in：最后被搜索，包含内建名字的最外层作用域。
   属性名称：对象命名空间
   点号的属性名指的是特定对象的属性，并且遵循属性和类的规则，就雷和实例对象而言，引用规则
   则增加了继承搜索这个流程
   赋值语句（object.X = value）
      在进行点号运算的对象的命名空间内创建或修改属性名X。继承树的搜索只发生在属性引用时，
   引用（object.X） 
      就基于类的对象而言，会在对象内搜索属性名X，然后是其上所有读取的类（用来继承搜索流程）。
      对于不是基于类的对象而言（例如模块），则是从对象中直接读取X。
   
   

    """

    # print(X)
    # f()
    # g()
    # print(X)
    obj = C()
    # class name inherited by instance 给实例obj的空间变量添加一个变量X
    print(obj.X)
    # Attach attribute name X to instance now 将m属性添加到空间变量
    # 只有当函数调用或者方法执行时，局部变量才会存在内存中。
    obj.m()
    print(obj.X)
    print(C.X)
