class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        mins = [0]*n
        stack = []
        for i in range(n):
            #track your current minimum
            if i !=0:
                if nums[i] < nums[mins[i-1]]:
                    mins[i] = i
                else:
                    mins[i] = mins[i-1]
            # find your previous greather element
            while stack and nums[stack[-1]] <= nums[i]:
                idx = stack.pop()
            if stack:
                # if the current number is greather than his 
                #previus greathest element min we found answer
                if nums[i] > nums[mins[stack[-1]]]:
                    return True
            stack.append(i)
        return False