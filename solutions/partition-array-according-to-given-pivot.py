class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less =[]
        eq = []
        great = []
        res = []
        for e in nums:
            if e < pivot:
                less.append(e)
            elif e == pivot:
                eq.append(e)
            else:
                great.append(e)
        res.extend(less)
        res.extend(eq)
        res.extend(great)
        return res