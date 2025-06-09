from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## Approach: 2 pass solution
        # KEY FACT: n XOR n = 0
        # Calculate the XOR for all numbers in nums
        # Calculate the XOR for all numbers in range [0,n]
        # The final XOR between the two will return the missing num since it has only been XORed once
        numsXor = nums[0]
        for i in range(1, len(nums)):
            numsXor = numsXor ^ nums[i]
        
        actualXor = 0
        for num in range(1, len(nums)+1):
            actualXor = actualXor ^ num
        
        return actualXor ^ numsXor