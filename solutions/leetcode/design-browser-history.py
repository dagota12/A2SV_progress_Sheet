class Node:
    def __init__(self,url,prev=None,next = None):
        self.url = url
        self.next = next
        self.prev = prev
class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        newnode = Node(url)
        newnode.prev = self.curr
        self.curr.next = newnode
        self.curr = self.curr.next
        # self.disp()

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev and i < steps:
            self.curr = self.curr.prev
            i += 1
        # self.disp()
        return self.curr.url


    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next and i < steps:
            self.curr = self.curr.next
            i+=1
        # self.disp()
        return self.curr.url
    def disp(self):
        k = self.head; s = ""
        while k:
            s += f"{k.url} ->"
            if k == self.curr:
                break
            k = k.next
        print(s)



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)