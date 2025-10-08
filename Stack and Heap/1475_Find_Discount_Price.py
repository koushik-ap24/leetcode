from collections import deque
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ## Approach: Monotonic stack to find the next smaller element to the right
        # Intuition: For each price, we want to find the next price that is less than or equal to it
        # So monotonic stack will help us maintain a decreasing sequence of prices
        ## TC: O(n), SC: O(n)
        stack = deque([])
        answer = prices.copy()
        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]
            while len(stack) and stack[-1] > price:
                stack.pop()
            
            if len(stack):
                answer[i] = price - stack[-1]
            
            stack.append(price)
        
        return answer