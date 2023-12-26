class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        res=[]
        for e in nums:
            if e < 0:
                neg.append(e)
            else:
                pos.append(e)
        p1 = 0
        p2 = 0
        turn = True
        while p1<len(neg) or p2<len(pos):
            if turn:
                res.append(pos[p1])
                p1+=1
                turn = False
            else:
                res.append(neg[p2])
                p2+=1
                turn = True
        return res