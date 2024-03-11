class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_small, prev_small = [n]*n, [-1]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                curr_top = stack.pop()
                next_small[curr_top] = i
            if stack:
                prev_small[i] = stack[-1]
            stack.append(i)
        max_area = float('-inf')
        for i in range(n):
            width = next_small[i] - prev_small[i] - 1
            max_area = max(max_area,heights[i] * width)
        return max_area

