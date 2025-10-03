class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        firstPage = Node(homepage)
        self.head = Node(-1, firstPage)
        self.tail = Node(-2, None, firstPage)
        self.currPage = firstPage

        firstPage.next = self.tail
        firstPage.prev = self.head

    def visit(self, url: str) -> None:
        newPage = Node(url, self.tail, self.currPage)
        self.currPage.next = self.tail.prev = newPage
        self.currPage = newPage

    def back(self, steps: int) -> str:
        while self.currPage.prev != self.head and steps > 0:
            self.currPage = self.currPage.prev
            steps -= 1

        return self.currPage.val

    def forward(self, steps: int) -> str:
        while self.currPage.next != self.tail and steps > 0:
            self.currPage = self.currPage.next
            steps -= 1

        return self.currPage.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)