class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ev = sum([i for i in nums if i % 2 == 0])
        
        res = []
        for op in queries:
            v,i = op

            if (nums[i] + v) % 2 == 0:
                if  nums[i]%2 == 1:
                    ev += nums[i] + v
                else:
                    ev += v
            else:
                if nums[i]%2 == 0:
                    ev-=nums[i]

            res.append(ev)
            nums[i] = nums[i] + v
        return res



        