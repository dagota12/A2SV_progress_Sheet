class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l,r,best = 0 ,max(houses[-1],heaters[-1]),-1
        while l <= r:
            range_ = l + (r-l)//2
            coverd = True
            # implement range
            h,ht = 0,0
            while h < len(houses) and ht < len(heaters):
                ranges = (heaters[ht] - range_, heaters[ht] + range_)
                if houses[h] >= ranges[0] and houses[h] <= ranges[1]:
                    h += 1
                else:
                    ht += 1
            if h != len(houses):
                coverd = False

            if coverd:
                r = range_ - 1
                best = range_
            else:
                l = range_ + 1
        return best



