学习笔记
#python 类
## 类属性与对象属性
类属性在类中只保存一份
对象属性在每个对象中一份
对象实例化之后，引用一个不存在的的属性，python会自动创建此属性
## 类的属性作用域
内置类型不能增加属性和方法
类添加属性方法一：
obiect.newattr = value
方法二：
setattr(object,'newattr','value')
```
#人为约定不可修改
_name
#私有属性
__
#魔术方法
__method__
```
# 方法
三种方法：
普通方法 至少一个self参数，表示该方法的对象
``` 
def instance_method(self):
```
类方法   至少一个cls参数，表示该方法的类
```
@classmethod
def class_method(cls):
```
静态方法 由类调用，无参数
```
@staticmethod
def static_method():
```
## 静态方法描述器
静态方法不能使用类属性和实例属性
# 属性
## 属性的处理
__getattribute__()与__getattr__()都是对实例属性进行获取拦截
__getattribute__()对所有属性的访问都会调用该方法
__getattr__()适用于未定义的属性
实例取一个属性时会调用__getattribute__()方法
同时定义__getattribute__()与__getattr__()方法，先调用__getattribute__()再调用__getattr__(),如无返回，去__dict()__查找。
## property描述符
@property 将方法封装成属性
```
@property
def method(self,value):
    self._item = value
```
@method.setter 支持修改
```
@method.setter
def method(self,value):
    self._item = value
```
@method.deleter
```
def method(self):
    del self._item
```
# 继承
当前类或父类继承了object类，那么该类是新式类
##object类与type类关系
object类与type都属于type类
object类由元类type创建
object类的父类为空，type类的父类为object
##钻石继承
当父类有同名方法时，python3采用广度优先的方式进行继承
subclass.mro()可以帮助查看继承关系
有向无环图判断继承关系
python没有实现重载功能
#设计模式
solid设计原则：
单一责任原则
开放封闭原则
里氏替换原则
依赖倒置原则
接口分离原则
##单例模式
__init__ 和 __new__的区别：
__new__ 是实例创建之前被调用，静态方法，返回该实例对象
__init__ 是实例方法，在实例被创建后调用
__new__先调用，__init__后调用
__new__将返回值传递给 __init__的第一个参数
单例模式实现：
使用函数装饰器实现
```
def singleton(cls):
    instance = {}
    getinstance(cls):
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]
    return getinstance(cls)
@singleton
class exp():
    pass
```
使用 __new__实现
```
import threading
class singleton(object):
    objs = {}
    obj_lock = threading.lock()
    def __new__(cls,*args,**kargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.obj_lock.acquire()
        try:
            if cls in cls.objs:
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()     
```
## 抽象基类
```
from abc import ABCMeta, abstractmethod
class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass
```
## Mixin 模式（动态继承）
```
def mixin(Kclass,MixinKlass)
    Kclass.__base__ = (MixinKlass,)+kclass.__base__
```
