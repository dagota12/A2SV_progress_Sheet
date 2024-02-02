# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = set()
        i = 0
        index = defaultdict(int)
        curr = head
        while curr and curr.next:
            if curr in visited:
                return curr
            index[curr] = i
            visited.add(curr)
            curr = curr.next
            i += 1
        return None