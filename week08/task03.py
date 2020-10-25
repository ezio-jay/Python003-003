import time
def timer(func):
    def inner(*args,**kargs):
        start_time = time.time()
        func(*args,**kargs)
        print(f'run time is {time.time()-start_time}')
    return inner

@timer
def test_func(sleep_time):
    time.sleep(sleep_time)

if __name__ == "__main__":
    test_func(5)