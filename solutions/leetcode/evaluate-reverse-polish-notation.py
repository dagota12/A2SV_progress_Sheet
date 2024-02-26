class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if not ch in "+-*/":
                stack.append(int(ch))
            else:
                y = stack.pop()
                x = stack.pop()
                if ch == '+':
                    stack.append(x+y)
                elif ch == '-':
                    stack.append(x - y)
                elif ch == '*':
                    stack.append(x*y)
                else:
                    stack.append(int(x/y))
        return stack[-1]