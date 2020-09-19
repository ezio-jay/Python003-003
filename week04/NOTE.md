学习笔记
[pandsa文档](https://www.pypandas.cn/)
[Numpy文档](https://numpy.org/doc/)
[matplotlib文档](https://matplotlib.org/contents.html)
#pandas基本数据类型
1.Series
```
#通过字典创建带索引的Series
s1 = pd.Series({'a':11,'b':22,'c':33})
#通过关键字创建带索引的Series
s2 = pd.Series([11,22,33],index = ['a','b','c'])
```
2.dataframe
```
#通过列表创建dataframe
df1 = pd.DataFrame(['a','b','c','d'])
#嵌套列表创建dataframe
df2 = pd.DataFrame(['a','b'],['c','d'])
#自定义列索引
df2.columns = ['1','2']
#自定义行索引
df2.index = ['one','tow']
```

