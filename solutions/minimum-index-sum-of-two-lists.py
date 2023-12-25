class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        mi = 10001
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i+j < mi:
                        mi = i+j
                        res = []
                        res.append(list1[i])
                    elif i+j == mi:
                        res.append(list1[i])
        return res


