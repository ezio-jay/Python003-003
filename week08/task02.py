def func_map(func,*iterable):
    for arg in zip(*iterable):
        yield func(*arg)

if __name__ =="__main__":
    iter = func_map(lambda x,y: x*y+1,[2,4,6,8,10],range(5))
    print(list(iter))