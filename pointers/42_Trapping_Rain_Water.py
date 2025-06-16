from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ## Approach 1: prefix and suffix max height arrays
        # TC: O(3n), SC: O(2n)
        n = len(height)
        prefixMax = [0] * n
        prefixMax[0] = height[0]
        for i in range(1,n):
            prefixMax[i] = max(height[i], prefixMax[i-1])
        
        suffixMax = [0] * len(height)
        suffixMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suffixMax[i] = max(height[i], suffixMax[i+1])
        
        res = 0
        for i in range(n):
            water = max(0, min(prefixMax[i], suffixMax[i]) - height[i])
            res += water
        
        return res

        ## Approach 2: Two pointers
        # TC: O(n), SC: O(1)
        # We only need to check the bottleneck height at the left and right pointers (Similar to container with most water problem)
        left, right = 0, len(height)-1
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
        return res
