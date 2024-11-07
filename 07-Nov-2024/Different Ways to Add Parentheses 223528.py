# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        oprs = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
        }
        memo = {}
        def backtrack(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            res = []
            for i in range(l,r+1):
                curr = expression[i]
                if curr in oprs:
                    left = backtrack(l,i-1)
                    right = backtrack(i+1,r)
                    for n1 in left:
                        for n2 in right:
                            res.append(oprs[curr](n1,n2))
            if not res:
                return [int(expression[l:r+1])]
            memo[(l,r)] = res
            return res
        n = len(expression)
        return backtrack(0,n-1)