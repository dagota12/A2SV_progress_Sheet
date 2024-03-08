# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.diff = float('-inf')
        def max_diff(node,curr_max = float('-inf'),curr_min = float(inf)):
            if not node:
                return 
            if float('-inf') != curr_max:
                self.diff = max(self.diff,abs(curr_max - node.val))
            if float('inf') != curr_min:
                self.diff = max(self.diff,abs(curr_min - node.val))            
            curr_max = max(curr_max,node.val)
            curr_min = min(curr_min,node.val)

            max_diff(node.left,curr_max,curr_min)
            max_diff(node.right,curr_max,curr_min)
        max_diff(root)
        return self.diff

