class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        queries = [0] * n
        for l,r in requests:
            queries[l] += 1
            if r + 1 < n:
                queries[r+1] -= 1
        for i in range(1,n):
            queries[i] +=  queries[i-1]
        queries.sort()
        nums.sort()
        max_sum = 0
        for x,q in zip(nums,queries):
            max_sum += x*q
        return max_sum%(10**9 + 7)