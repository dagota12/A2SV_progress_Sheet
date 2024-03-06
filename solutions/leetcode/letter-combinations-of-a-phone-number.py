class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hm = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        def backtrack(left =0,ans =[]):
            if left >= len(digits):
                if len(ans) == len(digits) and  ''.join(ans) != '':
                    res.append(''.join(ans))
                return
            for ch in hm[int(digits[left])]:
                ans.append(ch)
                backtrack(left+1,ans)
                ans.pop()
        backtrack()
        return res