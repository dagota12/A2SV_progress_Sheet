class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        idx = -1
        s = list(palindrome)
        for i,ch in enumerate(s):
            if ch != 'a':
                check = s.copy();check[i] = 'a'
                print(check)
                if check != list(reversed(check)):
                    idx = i
                    break
        if idx != -1:
            s[idx] = 'a'
        else:
            s[-1] = 'b'
        return ''.join(s)

