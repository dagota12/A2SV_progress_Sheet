# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.data = Counter()
    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        self.data[node.val] += 1
        self.inorder(node.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        modes = []
        items = self.data.items()
        max_ = max(items, key =lambda x:x[1])
        # print(max_)
        for num,f in self.data.items():
            if f == max_[1]:
                modes.append(num)
        return modes