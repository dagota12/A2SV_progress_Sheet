class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(str(y) + str(x)) - int(str(x) + str(y))
        arr = list(map(str, sorted(nums, key=cmp_to_key(compare))))
        
        return ("".join(arr)) if arr[0] != "0" else '0'