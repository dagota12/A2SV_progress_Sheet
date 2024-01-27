class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passagers = [0]*10001

        for number_of_passagers, start, end in trips:
            passagers[start] += number_of_passagers
            passagers[end] -= number_of_passagers
            
        for i in range(1,len(passagers)):
            passagers[i] += passagers[i-1]
        return max(passagers) <= capacity