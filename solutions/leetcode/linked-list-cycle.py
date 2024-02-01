# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head 
        flag = True # indicates if it is our first itration
        while fast and fast.next:
            if not flag and slow == fast:
                return True
            flag = False
            slow = slow.next
            fast = fast.next.next
        return False
