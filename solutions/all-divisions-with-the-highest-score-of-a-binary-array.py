class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score = {}
        tot_ones = nums.count(1)
        zeros = 0
        ones = 0
        
        for i,e in enumerate(nums):
            score[i] = zeros+ tot_ones - ones
            if e == 0:
                zeros+=1
            else:
                ones+= 1

        score[len(nums)] = zeros       
        mx = 0

        for items in (score.items()):
            if items[1] >= mx:
                mx = items[1]
        res = []

        for items in (score.items()):
            if items[1] == mx:
                res.append(items[0])

        return res