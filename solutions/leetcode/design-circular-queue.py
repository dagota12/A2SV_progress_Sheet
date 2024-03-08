class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.size = k
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.len == self.size:
            return False
        self.queue.append(value)
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            self.len -= 1
            return True
        return False

    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1  

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()