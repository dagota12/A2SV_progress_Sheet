class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        s = len(nums)
        r= s-1
        count = 0
        while l<=r:
            if nums[l]!=val:
                l+=1
                continue
            elif nums[r] == val:
                count+=1
                r-=1
                continue
            nums[l] = nums[r]
            count+=1
            l+=1
            r-=1
        return s-count
        
