class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.stack_top = None
        
    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.stack_top = x
   
    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.stack_top = self.queue1.popleft()
            self.queue2.append(self.stack_top)
        result = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result
        
    def top(self) -> int:
        return self.stack_top

    def empty(self) -> bool:
        return len(self.queue1) == 0