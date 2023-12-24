class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        p1 = 0
        p2 = n
        while p1 < n and p2<2*n:
            res.extend([ nums[p1],nums[p2] ])
            p1+=1
            p2+=1
        return res