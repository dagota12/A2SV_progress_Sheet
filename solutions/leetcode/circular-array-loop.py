class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = set()
        for i in range(n):

            if i not in visited:
                cycle = set()
                while True:
                    if i in cycle:
                        return True
                    visited.add(i)
                    cycle.add(i)
                    prev, i = i, (i+nums[i])%n # i becomes the next destination
                    if prev == i:# b/c we need acycle with more than 1 length
                        break
                    if nums[prev] >0 and nums[i]<0:# b/c should be same sign 
                        break

        return False
         
