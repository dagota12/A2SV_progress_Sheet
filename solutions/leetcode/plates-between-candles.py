class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles =[]
        plates = []
        for ch in s:
            if ch == '|':
                candles.append(1)
                plates.append(0)
            else:
                plates.append(1)
                candles.append(0)
        
        candles_p,plates_p,running_c,running_p = [0],[0],0,0
        for i in range(len(candles)):
            running_c += candles[i]
            running_p += plates[i]
            candles_p.append(running_c)
            plates_p.append(running_p)

        res = [] #0]*len(queries)
        for left,right in queries:
            l,r =left,right
            if s[l] != '|':
                l = min(len(candles_p)-1,bisect_right(candles_p,candles_p[l]))
            if s[r] != '|':
                r = bisect_left(candles_p,candles_p[r])

            if r>= l:
                res.append(plates_p[r] - plates_p[l])
            else:
                 res.append(0)
        return res
            
        