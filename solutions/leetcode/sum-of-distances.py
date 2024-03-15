class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        occures = defaultdict(list)
        for i,e in enumerate(nums):
            occures[e].append(i)
        res = [0]*len(nums)
        for occur in occures.values():
            prefix,postfix = occur.copy(), occur.copy()
            n = len(occur)
            for i in range(1,n):
                prefix[i] += prefix[i-1]
                postfix[n-1-i] += postfix[n-i]
            for i,idx in enumerate(occur):
                prev = prefix[i-1] if i-1 >= 0 else 0
                nxt = postfix[i + 1] if i+1 < len(occur) else 0
                res[idx] = (idx*i - prev) + nxt - (( len(occur) -1- i) * idx)
            # print(prefix,postfix)
        return res
            
            
