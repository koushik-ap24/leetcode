from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = profit = 0
        startNum = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < startNum:
                startNum = prices[i]
                continue
            
            profit = prices[i] - startNum
            if profit > result:
                result = profit
        
        return result