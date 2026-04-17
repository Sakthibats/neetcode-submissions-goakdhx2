from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = deque()
        self.summ = 0
        self.count = 0
        

    def next(self, val: int) -> float:
        if self.count==self.size:
            item = self.arr.popleft()
            self.summ += val - item
        else:
            self.count +=1
            self.summ += val
        self.arr.append(val)
        return self.summ/self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
