from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if len(head) < 2:
            return head
        
        curr = head
        prev = None
        newCurr = None

        while curr != None:
            newCurr = curr.next
            curr.next = prev
            prev = curr
            curr = newCurr
        
        return prev
