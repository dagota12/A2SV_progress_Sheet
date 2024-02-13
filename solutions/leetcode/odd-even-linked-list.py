# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        evens = head # even indexes 0,2,4,..
        odds = head.next # odd indexes 1,3,5....
        even_head = head.next
        # b/c odd pointer is allways will be at front only check odd
        while odds and odds.next: 
            evens.next = evens.next.next
            odds.next = odds.next.next # make the next of current-odd to next-idx(next-odd)
            evens = evens.next
            odds = odds.next # shift yr pointers
        evens.next = even_head
        return head




