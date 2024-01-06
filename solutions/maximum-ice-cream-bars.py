class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = Counter(costs)
        items = list(freq.items())
        items.sort(key = lambda x: x[0])
        cream = 0
        for k,v in items:
            cost = k
            count = v
            good = True
            while count > 0:
                if coins - cost < 0:
                    return cream
                coins-= cost
                cream += 1
                count-=1 
        return cream