# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:
    def __init__(self, max_size: int):

        self.stack = []
        self.size = max_size

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)