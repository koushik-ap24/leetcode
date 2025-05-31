from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # left to right - least to most significant in number

        carry = 0
        curr1 = l1
        curr2 = l2

        head = None
        prev = head

        while curr1 or curr2 or carry > 0:
            sum = 0
            if curr1 != None:
                sum += curr1.val
                curr1 = curr1.next
            if curr2 != None:
                sum += curr2.val
                curr2 = curr2.next
            
            sum += carry
            carry = sum // 10
            node = ListNode((sum % 10))

            if not head:
                head = node
            
            if prev != None:
                prev.next = node
            
            prev = node
        
        return head
