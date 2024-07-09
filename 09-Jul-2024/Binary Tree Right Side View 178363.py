# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels  = defaultdict(list)
        def dfs(node,lvl):
            if not node:
                return
            levels[lvl].append(node.val)
            dfs(node.left,lvl + 1)
            dfs(node.right,lvl + 1)
        dfs(root,0)
        res = []
        for row in levels.values():
            res.append(row[-1])
        return res