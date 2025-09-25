from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        ## Approach: Find the rightmost pivot where nums[pivot] < nums[pivot+1]
        # Intuition: Everything to the right of pivot is in descending order
        # Then find the smallest number to the right of pivot that is greater than nums[pivot]
        # Swap these two numbers
        # Finally, sort the subarray to the right of pivot in ascending order (or reverse since it's guaranteed to be in descending order)
        # TC: O(n), SC: O(1)
        
        n = len(nums)
        left = n-2

        while left >= 0 and nums[left] >= nums[left+1]:
            left -= 1
        
        if left < 0:
            nums.sort()
        else:
            right = n-1
            while nums[right] <= nums[left]:
                right -= 1
            nums[right], nums[left] = nums[left], nums[right]

            # bubble sort
            for i in range(left+1, n):
                flag = False
                for j in range(left+1, left+1+(n - i - 1)):
                    if nums[j] > nums[j+1]:
                        nums[j],nums[j+1] = nums[j+1],nums[j]
                        flag = True
                if not flag:
                    break