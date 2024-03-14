class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp_table = defaultdict( int )
        
        def optimal_pick( nums: List, left: int, right: int,l = 0):
            if left == right:
                return nums[left]
            
            if (left, right) in dp_table:
                return dp_table[ (left, right) ]
            
            choose_left = nums[left] - optimal_pick( nums, left+1, right,l+1 )
            choose_right = nums[right] - optimal_pick( nums, left, right-1,l+1 )
            dp_table[ (left, right) ] = max( choose_left, choose_right)
            return dp_table[ (left, right) ] 

        res = optimal_pick( nums, left = 0, right = len(nums)-1 )
        return res >= 0