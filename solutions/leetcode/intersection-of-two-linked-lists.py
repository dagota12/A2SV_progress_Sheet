# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A,B = set(),set()
        p1,p2 = headA,headB
        while p1:
            A.add(p1)
            p1 = p1.next
        while p2:
            if p2 in A:
                return p2
            p2 = p2.next
        return 
        