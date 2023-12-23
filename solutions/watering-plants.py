class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        st = 0
        c = capacity
        for i in range(len(plants)):
            if c >= plants[i]:
                st+=1
                c-=plants[i]
            else:
                st+= 2*i + 1
                c= capacity
                c-= plants[i]
        return st

