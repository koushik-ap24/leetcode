from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftP = 0
        rightP = len(numbers) - 1
        sum = 0
        result = []
        while leftP < len(numbers) and rightP >= 0:
            sum = numbers[leftP] + numbers[rightP]
            if sum == target:
                result.append(leftP+1)
                result.append(rightP+1)
                break
            elif sum < target:
                leftP += 1
            else:
                rightP -= 1
        
        return result