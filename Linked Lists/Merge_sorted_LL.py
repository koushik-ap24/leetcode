from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        
        head = curr = None
        ptr1 = list1
        ptr2 = list2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                if not curr:
                    curr = head = ptr1
                else:
                    curr.next = ptr1
                
                curr = ptr1
                ptr1 = ptr1.next
            
            else:
                if not curr:
                    curr = head = ptr2
                else:
                    curr.next = ptr2
                
                curr = ptr2
                ptr2 = ptr2.next
        
        curr.next = ptr1 if ptr1 else ptr2
        return head





        