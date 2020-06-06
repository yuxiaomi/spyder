# 抽象方法 抽象类
# class base(object):
#     def send(self):
#         raise NotImplementedError("子类中必须实现的方法")
#
# class foo(base):
#     def send(self):
#         print("test")
# obj=foo()
# obj.send()

#继承+抛出异常
import abc
# 指定类由那个type创建
class base(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send(self):pass
    def func(self):
        print("1234test")
class foo(base):
    def send(self):
        print("发送信息")
obj=foo()
obj.send()
obj.func()