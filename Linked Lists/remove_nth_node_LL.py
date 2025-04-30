from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:
            return None
        

        # reverse list
        curr = head
        prev = None
        oldNext = None
        while curr != None:
            oldNext = curr.next
            curr.next = prev
            prev = curr
            curr = oldNext
        
        # Find the node to be removed
        reversed_head = prev
        curr = reversed_head
        prev = None
        count = 1
        while count != n:
            prev = curr
            curr = curr.next
            count += 1
        
        if prev == None:
            reversed_head = curr.next
        else:
            prev.next = curr.next
        
        # reverse list
        curr = reversed_head
        prev = None
        oldNext = None
        while curr != None:
            oldNext = curr.next
            curr.next = prev
            prev = curr
            curr = oldNext
        
        return prev