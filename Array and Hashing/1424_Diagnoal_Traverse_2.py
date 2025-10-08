from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ## Approach: Use a hashmap to group elements by their diagonal index (row + col)
        ## TC: O(n), SC: O(n)

        ROWS = len(nums)
        res = []

        diagMap = defaultdict(list)
        for row in range(ROWS-1, -1, -1):
            for col in range(len(nums[row])):
                diagMap[row+col].append(nums[row][col])
        
        for diag in range(len(diagMap)):
            for val in diagMap[diag]:
                res.append(val)
        
        return res

        # diagArr = []
        # for row in range(ROWS):
        #     for col in range(len(nums[row])):
        #         diagArr.append((row+col, col, nums[row][col]))
        
        # diagArr.sort()
        # for total, col, val in diagArr:
        #     res.append(val)
        
        # return res