from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        left = 1
        right = 0
        for num in nums:
            right += abs(num)
        right += 1

        while left <= right:
            mid = (left + right) // 2
            step = mid
            for num in nums:
                step += num
                if step < 1:
                    break
            
            if step >= 1:
                right = mid - 1
            else:
                left = mid + 1
        
        return left