from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left = 0
        right = len(heights)-1

        # Always move the pointer with the smaller value forward.
        # WHy? Because thats the limiting factor, we already have the largest area possible for that particular column, so move it hoping that the next one is larger.
        while left < right:
            res = max(res, (right - left) * min(heights[left], heights[right]))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return res