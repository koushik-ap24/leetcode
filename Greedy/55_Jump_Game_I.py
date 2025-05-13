from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # No need to find optimal soln, only find if you can reach the end
        # Goalpost solution
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
            
        return goal == 0