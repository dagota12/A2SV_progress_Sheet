class Solution:
    def fib(self, n: int,memo = {}) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 0
        elif n in memo:
            return memo[n]
        memo[n] = self.fib(n-1) + self.fib(n-2)
        return memo[n]