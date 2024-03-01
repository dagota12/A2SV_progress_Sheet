# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((0,root))
        data = defaultdict(list)
        while queue:
            l,curr = queue.popleft()
            if curr:
                data[l].append(curr.val)
                queue.append((l+1,curr.left))
                queue.append((l+1,curr.right))
        return [item[1] if item[0]%2 == 0 else item[1][::-1] for item in data.items()]
    