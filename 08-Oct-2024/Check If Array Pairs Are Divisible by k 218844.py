# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, nums: List[int], k: int) -> bool:
        freq = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            if  (k - nums[i] % k) in freq:
                freq[ k - nums[i] % k] -= 1
            else:
                freq[nums[i] % k] += 1
        for k in freq:
            if 0 in freq and freq[k]%2 == 0:
                continue
            if freq[k] != 0:
                return False
        return True

        """
        arr = [1,2,3,4,5,10,6,7,8,9], k = 5
        the sum of the arr is 55 and its divisible by 5 if we created a group pf 2 
        we end up with 5 groups with each summig to 11 so if we mod each number
        by eleven...
        for the first element we can see [1,10] are match but lets verify
        remainder 1%11 = 1 the remainder is one
        10 % 11 = remainder ten how do i know there is a matching in 
        map well if i subtract the mod from the required sum in this case 11 
        11 - 10 which is 1 and i know it exists in my map

        the last part is just checking if all the numbers got their match

        """