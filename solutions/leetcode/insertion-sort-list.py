# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums= []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        
        for i in range(1,len(nums)):
            curr = nums[i]
            j = i-1
            while j >=0 and nums[j] > curr:
                nums[j+1] = nums[j]
                j -= 1
            nums[j + 1] = curr

        cur = head
        i = 0
        while cur:
            cur.val = nums[i]
            cur = cur.next
            i+=1
        return head