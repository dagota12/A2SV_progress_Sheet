# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, root, k):
        
        parts = [None for i in range(k)]

        size = 0
        node = root
        while node: # calculate size
            size += 1
            node = node.next
        n, rem = size//k , size%k

        node = root
        prev = None
        for i in range(k):
            parts[i] = node
            remaining = 1 if rem > 0 else 0

            for j in range(n + remaining):
                prev = node
                node = node.next
            rem -= 1

            if prev:
                prev.next = None

        return parts