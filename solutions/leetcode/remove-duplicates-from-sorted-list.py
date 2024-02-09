# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,None)
        ptr = dummy
        curr = head
        prev = None
        while curr:
            if prev != None and curr.val == prev:
                curr = curr.next
                continue
            ptr.next = ListNode(curr.val)
            ptr = ptr.next
            prev = curr.val
            curr = curr.next
        return dummy.next

