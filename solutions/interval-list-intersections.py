class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1,p2 =0,0
        res = []
        while p1 < len(firstList) and p2 < len(secondList):
            first = firstList[p1]
            second = secondList[p2]
            if first[0] >= second[0] and first[1] <= second[1]:
                res.append([first[0],first[1]])
                p1 += 1
            elif first[0] <= second[0] and first[1] >= second[1]:
                res.append([second[0],second[1]])
                p2+=1
            elif first[0] <= second[0] and first[1] >= second[0] and first[1] <= second[1]:
                res.append([second[0],first[1]])
                p1+=1
            elif first[1] >= second[0] and first[0] >= second[0] and first[0] <= second[1]:
                res.append([first[0],second[1]])
                p2+=1
            else:
                if first[1] < second[0]:
                    p1+=1
                else:
                    p2+=1
        return res

       