class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * len(s)
        res = ""
        for l,r,f in shifts:
            if f == 1:
                shift[l] += 1
                if r+1< len(shift):shift[r+1] -= 1
            else:
                shift[l] -= 1
                if r+1< len(shift):shift[r+1] += 1
        acc = 0
        for i  in range(len(s)):
            acc+= shift[i]
            c = (ord(s[i]) - ord('a') + acc)%26
            if c < 0: c += 26
            c+= + ord('a')
            res+= chr(c)
        return res