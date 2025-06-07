from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach:
        # Use XOR to find the single number
        # Xor finds the single number because xor of a number with itself is 0, regardless of the order or if the number appears much later.
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        
        return res