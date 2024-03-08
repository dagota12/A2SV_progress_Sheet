# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        def traverse(node,r=0,c=0):
            if not node:
                return
            traverse(node.left,r+1,c-1)
            cols[(r,c)].append(node.val)
            traverse(node.right,r+1,c+1)
        traverse(root)
        for arr in cols.values():
            arr.sort()
        pre_ans = defaultdict(list)
        for k,val in sorted(cols.items(),key = lambda x:x[0][0] - x[0][1]):
            r,c = k
            pre_ans[c].extend(val)
        ans = []
        for i,arr in sorted(pre_ans.items()):
            ans.append(arr)
        return ans
