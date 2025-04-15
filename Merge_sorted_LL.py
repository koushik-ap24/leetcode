from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        ptr1 = list1
        ptr2 = list2
        merged = None
        newNext = None

        if ptr1.val <= ptr2.val:
            merged = ptr1
            newNext = ptr1.next
            ptr1.next = None
            ptr1 = newNext
        else:
            merged = ptr2
            newNext = ptr2.next
            ptr2.next = None
            ptr2 = newNext

        ptr_merged = merged

        while ptr1 != None and ptr2 != None:
            if ptr1.val > ptr2.val:
                print(f"branch 1")
                ptr_merged.next = ptr2
                ptr_merged = ptr2
                newNext = ptr2.next
                ptr2.next = None
                ptr2 = newNext
            else:
                print(f"branch 2")
                ptr_merged.next = ptr1
                ptr_merged = ptr1
                newNext = ptr1.next
                ptr1.next = None
                ptr1 = newNext
        
        ptr_merged.next = ptr1 or ptr2

        return merged





        