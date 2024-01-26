class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        frequency = defaultdict(int)
        count = 0
        for i,num in enumerate(nums):
            #if the current number is valid
            if num == k:
                count += 1
            if num - k in frequency:
                # this formula works b/c if we subtract <k>  from the current 
                # number from it allways gives us the number just the
                # starting point where our sum start eg: k = sum(nums[a[i:j]])
                # prefix_sum[j] - k will give prefix_sum[i-1] if the sum exists
                # add the count of those numbers b/c it's going to work for all
                count += frequency[num-k]
            frequency[num] += 1
        return count

            
            
        

