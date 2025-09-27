from collections import deque
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      ## Approach: Monotonic Stack
      # Intuition: We can use a stack to keep track of the next greater elements as we iterate through nums2 in reverse order.
      # For each element in nums2, we pop elements from the stack until we find a greater element or the stack is empty.
      # Similar to Online Stock Span and Daily Temperatures problems.
      ## TC: O(n+m), SC: O(n)
      
        nums2Map = {}
        for i, val in enumerate(nums2):
            nums2Map[val] = i

        n = len(nums2)
        nextGreatest = [-1] * n
        stack = deque([])
        for i in range(n-1, -1, -1):
            while len(stack) and stack[-1] < nums2[i]:
                stack.pop()
            
            if len(stack):
                nextGreatest[i] = stack[-1]
            
            stack.append(nums2[i])
        
        res = []
        for query in nums1:
            idx = nums2Map[query]
            res.append(nextGreatest[idx])
        
        return res