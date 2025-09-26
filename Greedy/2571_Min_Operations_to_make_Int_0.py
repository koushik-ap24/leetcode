import math


class Solution:
    def minOperations(self, n: int) -> int:
        ## Approach: Recursion + Math
        # Intuition: The fastest way to reduce a number to 0 is to subtract the closest power of 2 from it.
        # TC: O(log n), SC: O(log n)
        def dfs(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            power = int(math.log(n)/math.log(2))
            num1 = abs(2**power - n)
            num2 = abs(2**(power+1) - n)
            closest = min(num1,num2)

            return 1 + dfs(closest)
        
        return dfs(n)