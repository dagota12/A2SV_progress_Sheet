# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = 0
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def max_sum(node,l=0):
            # print(f"{'  '*l}lvl:{l} state:",node.val if node else None)
            if not node:
#               return is_BST,left_max, right_min, current_sum                
                return (True,float('-inf'),float('inf'),0)

            islbst, max_l, min_l, l_sum = max_sum(node.left,l+1)
            isrbst, max_r, min_r, r_sum = max_sum(node.right,l+1)

            # print(f"{'  '*l}level:{l}",islbst,max_l,min_l, l_sum)
            # print(f"{'  '*l}level:{l}",isrbst,max_r,min_r,r_sum)

            if islbst and isrbst and max_l < node.val and min_r > node.val:
                new_sum = l_sum + r_sum + node.val
                self.max_sum = max(self.max_sum, new_sum)
                return (True,max(node.val,max_r),min(node.val,min_l),new_sum)
            return (False,float('-inf'),float('inf'),0)
        max_sum(root)
        return self.max_sum
            