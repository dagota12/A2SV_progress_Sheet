# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1 = ListNode()
        list2 = ListNode()
        p1,p2 = list1,list2
        curr = head
        while curr:
            if curr.val < x:
                p1.next = ListNode(curr.val)
                p1 = p1.next
            else:
                p2.next = ListNode(curr.val)
                p2 = p2.next
            curr = curr.next
        p1.next = list2.next
        return list1.next