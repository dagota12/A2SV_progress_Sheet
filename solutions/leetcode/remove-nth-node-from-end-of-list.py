# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummy = ListNode(0,head)
        curr = head
        while curr:
            size += 1
            curr = curr.next
        idx = size - n

        prev_node,i = dummy,0
        while prev_node and i < idx:
            prev_node = prev_node.next
            i += 1
        prev_node.next = prev_node.next.next
        return dummy.next
