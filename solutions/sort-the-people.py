class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = [[name,height] for name,height in zip(names,heights)]
        name_height.sort(reverse = True,key = lambda x: x[1])
        return [elem[0] for elem in name_height]