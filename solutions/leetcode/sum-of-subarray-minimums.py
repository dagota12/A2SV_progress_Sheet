class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prev_min, next_min = [-1]*n, [n]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                idx = stack.pop()
                next_min[idx] = i
            if stack:
                prev_min[i] = stack[-1]
            stack.append(i)

        sum_ = 0
        for i,vals in enumerate(zip(prev_min,next_min)):
            prev,next = vals
            sum_ += ((i - prev) * (next - i) * arr[i])
        return sum_ % (10**9 + 7)
