# 命名空间链接
# 实例和类的特殊属性__class__和__bases__ 可以再程序代码内查看继承层次
# 例如查看继承层次

def classtree(cls, indent):
    print("." * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)


def instancetree(inst):
    print("Tree of %s" % inst)
    classtree(inst.__class__, 3)


def selftest():
    class A: pass

    class B(A): pass

    class C(A): pass

    class D(B, C): pass

    class E: pass

    class F(D, E): pass

    instancetree(B())
    instancetree(F())



if __name__ == "__main__":
    selftest()
