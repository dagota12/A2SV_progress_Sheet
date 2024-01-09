class Solution:
    def smallestNumber(self, num: int) -> int:

        minimum = sorted(list(str(abs(num))),reverse = True)
        if(num < 0):
            return -1 * int("".join(minimum))
        
        i = 0
        minimum = minimum[::-1]
        while i < len(minimum) and minimum[i] == '0':
            i+= 1
        if i < len(minimum):
            minimum[i],minimum[0] = minimum[0],minimum[i]
        return  int("".join(minimum))
