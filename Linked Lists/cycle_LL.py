from typing import Optional

# Solution uses Floyd's Cycle detection algorithm (fast-slow pointer)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        fast_ptr = head
        slow_ptr = head

        while fast_ptr != None and fast_ptr.next != None:
            fast_ptr = (fast_ptr.next).next
            slow_ptr = slow_ptr.next

            if fast_ptr == slow_ptr:
                return True
        
        return False
        