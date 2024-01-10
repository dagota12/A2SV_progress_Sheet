class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        boats = 0
        p1 = 0
        p2 = len(people) - 1
        while p1 <= p2:
            if(people[p2] + people[p1] <= limit):
                p1 += 1
                p2 -= 1
            else:
                p2 -= 1
            boats += 1

        return boats

        

