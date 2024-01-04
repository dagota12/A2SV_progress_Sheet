class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}
        for i in range(len(arr2)):
            freq[arr2[i]] =  i
        res = []
        not_in = []
        for e in arr1:
            if e in freq:
                res.append(e)
            else:
                not_in.append(e)
        res.sort(key = lambda x: freq[x])

        not_in.sort()
        res.extend(not_in)
        return res