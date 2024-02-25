class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, n = [], len(nums)
        next_gr = [-1]*n
        for i in range(2):
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    idx = stack.pop()
                    next_gr[idx] = i
                stack.append(i)
        return ([nums[i] if i != -1 else -1 for i in next_gr])