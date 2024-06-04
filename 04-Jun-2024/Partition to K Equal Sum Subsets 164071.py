# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/


def set_bit(n,sh):
    return n | (1 << sh)
def unset_bit(n,sh):
    return n & ~(1 << sh)
def is_set(n,sh):
    return (n >> sh) & 1
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sm = sum(nums)
        n = len(nums)
        if sm % k != 0:
            return False
        req = sm//k
        memo={}
        nums.sort(reverse=True)
        def backtrack(curr_sum,mask):
            if (1<<(n))-1== mask:
                return curr_sum == req
            if curr_sum == req:
                return backtrack(0,mask)
            if (curr_sum,mask) not in memo:  
                temp=False
                for i in range(n):
                    if not is_set(mask,i) and curr_sum+nums[i] <= req:
                        temp=temp or backtrack(curr_sum+nums[i],set_bit(mask,i))
                    
                memo[(curr_sum,mask)]=temp
            return memo[(curr_sum,mask)]
            
        return backtrack(0,0)