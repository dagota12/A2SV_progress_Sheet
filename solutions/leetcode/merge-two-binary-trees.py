# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if (not root1) and (not root2):
            return None
        if (not root1) or (not root2):
            return root1 if  root1 else  root2
        val = 0
        if root1 and root2:
            val = root1.val + root2.val
        else:
            val = root1.val if root1 else root2.val
        new_node = TreeNode(val)
        new_node.left = self.mergeTrees(root1.left,root2.left)
        new_node.right = self.mergeTrees(root1.right,root2.right)
        return new_node