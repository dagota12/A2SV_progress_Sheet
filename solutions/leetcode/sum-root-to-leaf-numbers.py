# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(node,num=[]):
            if not node:
                return
            elif not node.left and not node.right:
                nums.append(int(''.join(num + [str(node.val)])))
                return

            num.append(str(node.val))
            dfs(node.left,num)
            dfs(node.right,num)
            num.pop()
        dfs(root)
        return sum(nums)
