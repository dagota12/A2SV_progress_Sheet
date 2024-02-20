class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        needed = 0
        for p in s:
            if p == '(':
                stack.append('(')
            else:
                if stack != []:
                    stack.pop()
                else:
                    needed += 1
        return needed + len(stack)
