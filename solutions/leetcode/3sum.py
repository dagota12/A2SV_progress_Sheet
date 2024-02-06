class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        collect=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]: continue
            l=i+1
            r= len(nums)-1
            target= -nums[i]
            while l<r:
                if l>i+1 and nums[l] == nums[l-1]:
                    l+=1
                    continue
                elif r< len(nums)-1 and nums[r] == nums[r+1]:
                    r-=1
                    continue
                if nums[l]+nums[r] == target:
                    collect.append([ nums[i],nums[l],nums[r] ])
                    l+=1
                    r-=1
                elif nums[l]+nums[r] > target:
                    r-=1
                elif nums[l]+nums[r] < target:
                    l+=1
                        
        return collect
            
        