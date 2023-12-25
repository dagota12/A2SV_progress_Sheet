class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count ={}
        res = set()
        goal = len(nums)//3
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
                if count[nums[i]] > goal:
                    res.add(nums[i])
            else: 
                count[nums[i]] = 1
                if count[nums[i]] > goal:
                    res.add(nums[i])
        return list(res)
            