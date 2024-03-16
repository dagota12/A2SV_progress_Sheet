class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r,best = max(weights),sum(weights),-1
        while l <= r:
            mid = l + (r-l)//2
            curr_days = 1
            curr = 0
            for i in range(len(weights)):
                curr += weights[i]
                if curr > mid:
                    curr_days += 1
                    curr = weights[i]
            if curr_days <= days:
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        return best
            
            
