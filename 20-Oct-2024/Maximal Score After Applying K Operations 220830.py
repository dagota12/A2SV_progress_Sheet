# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        mx_heap = [-x for x in nums]
        heapq.heapify(mx_heap)
        score = 0
        
        for i in range(k):
            val = -heapq.heappop(mx_heap)
            if val == 0:
                break
            score += val
            val = math.ceil(val/3)
            heapq.heappush(mx_heap,-val)
        return score

