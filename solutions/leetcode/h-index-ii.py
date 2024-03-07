class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r, best = 0, n, 0

        while l <= r:
            mid = l + (r-l)//2
            #calculate  current citations
            valid = True
            for i in range(n-1,n - 1 - mid,-1):
                if citations[i] < mid:
                    valid = False
                    break
            if valid:
                best = max(best,mid)
                l = mid + 1
            else:
                r = mid - 1
        return best

