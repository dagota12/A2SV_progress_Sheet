class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, n = [], len(temperatures)
        next_gr = [0]*n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                next_gr[idx] = i - idx
            stack.append(i)
        return next_gr