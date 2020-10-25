学习笔记
#函数工具与高阶函数
map
```
def square(x):
    return x**2

m = map(square, range(10))
next(m)
list(m)
[square(x) for x in range(10)]
dir(m)
```

reduce
```
# reduce(f, [x1, x2, x3]) = f(f(x1, x2), x3)
from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 9])
#25
```

# filter
```
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
```

# 偏函数
```
def add(x, y):
    return x + y

import functools
add_1 = functools.partial(add, 1)
add_1(10)

import itertools
g = itertools.count()
next(g)
next(g)
auto_add_1 = functools.partial(next, g)
auto_add_1()
```
#闭包
nonlocal 访问外部函数的局部变量
#装饰器
增强而不改变原有函数
装饰器强调函数的定义态而不是运行态
```
# 被修饰函数带参数
def outer(func):
    def inner(a,b):
        print(f'inner: {func.__name__}')
        print(a,b)
        func(a,b)
    return inner

@outer
def foo(a,b):
    print(a+b)
    print(f'foo: {foo.__name__}')
    
    
>>>foo(1,2)
inner:foo
1 2
3
foo:inner
```
## python 内置装饰器
@wraps接受一个函数来进行装饰
@functools.lru_cache() 将函数运行结果进行缓存
functools.lru_cache(maxsize=128, typed=False)有两个可选参数
maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放
typed若为True，则会把不同的参数类型得到的结果分开保存
## 类装饰器
利用__call__ 函数将类模拟成可调用对象
##异步编程
```
import asyncio
async def py35_coro():
    await stuff()
```
