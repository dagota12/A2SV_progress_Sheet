class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0,0,0]
        for e in nums:
            count[e] += 1
        colors = [0,1,2]
        i = 0
        j = 0
        # print(count.values())
        for val in count:
            temp = val
            while temp > 0 and j < len(colors):
                
                nums[i] = colors[j]
                temp-=1
                i+=1
            j+=1

        """
        Do not return anything, modify nums in-place instead.
        """
        