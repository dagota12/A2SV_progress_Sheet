class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                txt = []
                while stack and stack[-1] != '[':
                    txt.append(stack.pop())
                stack.pop()
                num = []
                while stack and  stack[-1].isdigit():
                    
                    num.append(stack.pop())
                num = int("".join(num[::-1]))
                stack.append("".join(txt[::-1])*num)
        return "".join(stack)