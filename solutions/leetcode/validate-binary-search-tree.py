# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,l=0):
            # print(f"{'  '*l}level:{l} state:",node.val if node else None)
            if not node:
                return (True,float('-inf'),float('inf'))
            islbst,max_l,min_l = valid(node.left,l+1)
            isrbst,max_r,min_r = valid(node.right,l+1)

            # print(f"{'  '*l}level:{l}",islbst,max_l,min_l)
            # print(f"{'  '*l}level:{l}",isrbst,max_r,min_r)

            if islbst and isrbst and node.val > max_l and node.val < min_r:
                return (True,max(node.val,max_r),min(min_l,node.val))
            return (False,-1,-1)
        return valid(root)[0]

