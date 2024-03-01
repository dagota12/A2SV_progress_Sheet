class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                curr_top = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[curr_top]
                    w = i - (stack[-1] + 1)
                    trapped += w*h
            stack.append(i)
        return trapped