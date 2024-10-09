# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] = arr[i] ^ arr[i-1]
        ans =  []
        for l,r in queries:
            res = arr[r] if l == 0 else arr[l-1] ^ arr[r]
            ans.append(res)
        return ans