from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque([])
        res = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                val, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temp, i))
        
        return res