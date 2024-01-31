class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        temp = self.head
        for i in range(index):
            if not temp:
                return            
            temp = temp.next
            if not temp:
                return -1
        return temp.val


    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = newnode
            self.size += 1
            return
        self.head = newnode
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        newnode = Node(val)
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        for i in range(index-1):
            if not temp:
                return                
            temp = temp.next
            if not temp:
                return
        if temp:
            newnode.next = temp.next
            temp.next = newnode
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        temp = self.head
        if index == 0:
            self.head = self.head.next
        for i in range(index-1):
            if not temp:
                return            
            temp = temp.next
            if not temp:
                return            
        if temp.next:
            temp.next = temp.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)