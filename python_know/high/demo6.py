# 用户自定义异常
class Bad(Exception):
    pass


try:
    a = 0
except Bad:
    print("got Bod")



try:
    b = 0
    print(b)
except IndexError:
    pass
except SyntaxError:
    pass
else:
    print("没有异常机就执行")
finally:
    print("我执行完了")







