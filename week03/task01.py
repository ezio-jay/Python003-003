import threading
import random
import time
class DiningPhilosophers(threading.Thread):
    def __init__(self,id,eat_times,left_fork,right_fork):
        threading.Thread.__init__(self) 
        self.id = id
        self.eat_times = eat_times
        self.left_fork = left_fork
        self.right_fork = right_fork
    def pickLeftFork(self):
        while True:
            if self.left_fork.acquire():
                output = [self.id,1,1]
                print(output)
                break
    def pickRightFork(self):
        while True:
            self.right_fork.acquire()
            output = [self.id,2,1]
            print(output)
            break
    def eat(self):
        self.eat_times -= 1
        time.sleep(4)
        output = [self.id,0,3]
        print(output)
    def putLeftFork(self):
        self.left_fork.release()
        output = [self.id,1,2]
        print(output)
    def putRightFork(self):
        self.right_fork.release()
        output = [self.id,2,2]
        print(output)
    def think(self):
        time.sleep(random.randint(1,10))
    def wantsToEat(self):
        self.think()
        self.pickLeftFork()
        self.pickRightFork()
        self.eat()
        self.putLeftFork()
        self.putRightFork()
    def run(self):
        while self.eat_times != 0:
            self.wantsToEat()
if __name__ == "__main__":
    froks = [threading.Lock() for i in range(5)]
    phis = []
    eat_times = int(input("输入吃饭次数"))
    for i in range(5):
        phi = DiningPhilosophers(i,eat_times,froks[(i+4)%5],froks[i])
        phis.append(phi)
    for phi in phis:
        phi.start()
    for phi in phis:
        phi.join()
