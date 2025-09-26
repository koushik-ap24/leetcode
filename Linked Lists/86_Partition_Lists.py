from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessHead = None
        lessPtr = None
        greaterHead = greaterPtr = None

        curr = head
        if not curr:
            return curr
        
        while curr != None:
            newNode = ListNode(curr.val)
            if curr.val < x:
                if not lessHead:
                    lessHead = lessPtr = newNode
                else:
                    lessPtr.next = newNode
                    lessPtr = newNode
            
            else:
                if not greaterHead:
                    greaterHead = greaterPtr = newNode
                else:
                    greaterPtr.next = newNode
                    greaterPtr = newNode
            
            curr = curr.next
        
        if not lessPtr:
            return greaterHead
        
        lessPtr.next = greaterHead
        return lessHead
