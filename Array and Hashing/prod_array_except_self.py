from typing import List

# My solution - using division method
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        zero_count = 0
        for i in range(1, len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_count += 1

        result = []
        for num in nums:
            if num == 0 and zero_count == 1:
                result.append(product)
            elif (num != 0 and zero_count == 1) or zero_count > 1:
                result.append(0)
            else:
                result.append(int(product/num))

        return result
    
# Recommended solution - prefix and suffix arrays
        