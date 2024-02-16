# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev,cur = ListNode(0,head),head
        i  = 0
        # move to the node before the reverse begins
        while cur and i < left - 1:
            prev = cur
            cur = cur.next
            i += 1
            # if starting of the revrsal is at the end don't do any thing
            if not prev:
                return head
    # start revesing
    # with each itreation move the currents next to the begning of the 
    # making out selfs before the starting point of reversal starting of the reversal <prev>
    # with each itreation move the <currents> next node next to prevs next
        while i < right - 1 and cur and cur.next:
            next_node = cur.next
            cur.next =  next_node.next
            next_node.next = prev.next
            prev.next = next_node
            i+=1
        if left == 1:
            return prev.next
        else:
            return head

            

        
        
