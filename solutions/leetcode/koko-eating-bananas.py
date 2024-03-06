class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r,best = 1, sum(piles),max(piles)

        while l <= r:
            mid = l + (r-l)//2
            time = 0
            for p in piles:
                time += ceil(p/mid)
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
                best = min(best,mid)
        return best
              