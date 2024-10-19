# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertReverse(txt):
            n = len(txt)
            res = [""]*n
            for i in range(n-1,-1,-1):
                if txt[i] == "1":
                    res[n-1 - i] = "0"
                else:
                    res[n-1 - i] = "1"
            return "".join(res)
        vals = ["0"]*n
        for i in range(1,n):
            vals[i] = "".join([vals[i-1], "1", invertReverse(vals[i-1])])
        return vals[n-1][k-1]
