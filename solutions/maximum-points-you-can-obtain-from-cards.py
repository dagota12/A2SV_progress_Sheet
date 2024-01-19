class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l = k - 1
        cur_sum = sum(cardPoints[:k])
        res = cur_sum
        for r in range(-1,-k-1,-1):
            cur_sum -= cardPoints[l]
            l-=1
            cur_sum += cardPoints[r]
            res = max(res,cur_sum)
        return res



