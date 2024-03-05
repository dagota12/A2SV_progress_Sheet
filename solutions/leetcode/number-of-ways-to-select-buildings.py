class Solution:
    def numberOfWays(self, s: str) -> int:
        freq = defaultdict(int)
        n10,n01 = 0,0
        tot = 0
        for num in s:
            if num == '0':
                n10 += freq[1]
                freq[0] += 1
            else:
                n01 += freq[0]
                freq[1] += 1
            if num == '0':
                tot += n01
            else:
                tot += n10
        return tot
