#python 多进程
##产生多进程的方式
1. 
```os.fork()
#得到进程ID
os.getpid()
```
2. multiprocessing.Process()
```
multiprocessing.Process(group=None,target=None,name=None,args=(),kwargs={})

# - group：分组，实际上很少使用
# - target：表示调用对象，你可以传入方法的名字
# - name：别名，相当于给这个进程取一个名字
# - args：表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入(m, n)即可
# - kwargs：表示调用对象的字典
```
3. 继承process类

## 进程间通信
利用 Queue类进行通信
```
from multiprocessing import Queue
```
利用管道进行通信
利用共享内存

