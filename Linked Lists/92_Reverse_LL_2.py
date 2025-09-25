from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Assumptions:
        # - list must contain at least one node
        # - nodes have unique values
        # - left <= right, 1-indexed

        ## Approach: Two-pass iterative
        # Intuition: First, identify the left and right boundaries and their previous/next nodes
        # Then, reverse the nodes between left and right using standard linked list reversal technique
        # Finally, reconnect the reversed sublist back to the main list
        ## TC: O(n), SC: O(1)


        if left == right:
            return head
        
        # Pass 1: Get the right references for left and right boundaries
        # Save the oldLeftBefore and oldRightNext for later use
        leftP = head
        leftPBefore = None
        curr = head
        index = 1
        rightP = head

        while index < right:
            if index == (left - 1):
                leftPBefore = curr
    
            if index == left:
                leftP = curr
            curr = curr.next
            index += 1
        
        rightP = curr
        oldRightNext = rightP.next

        ## Pass 2: Reversal
        # Reverse the nodes within the identified boundaries using standard LL reversal technique

        curr = head
        prev = None
        while prev != leftP:
            prev = curr
            curr = curr.next
        
        while prev != rightP:
            newCurr = curr.next
            curr.next = prev
            prev = curr
            curr = newCurr
        
        leftP.next = oldRightNext
        if left == 1:
            return rightP
        
        # If left is not head, then point its previous element to right (which is now at left due to reversal)
        leftPBefore.next = rightP
        return head