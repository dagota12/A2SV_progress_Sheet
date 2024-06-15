# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        def dfs(node):
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val in to_delete:
                if left:
                    res.append(left)
                if right:
                    res.append(right)
                return None
            node.left = left
            node.right = right
            return node

            
        dfs(root)
        if root and root.val not in to_delete:
            res.append(root)
        return res
