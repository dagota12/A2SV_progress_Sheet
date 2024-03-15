# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder = []
    def traverse(self,node):
        if not node:
            return
        self.traverse(node.left)
        self.inorder.append(node.val)
        self.traverse(node.right)
    def buildTree(self,arr):
        if not arr:
            return
        mid = len(arr)//2
        node = TreeNode(arr[mid])
        node.left = self.buildTree(arr[:mid])
        node.right = self.buildTree(arr[mid+1:])

        return node
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return self.buildTree(self.inorder)