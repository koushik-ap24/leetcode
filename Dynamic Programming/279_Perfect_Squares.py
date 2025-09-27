import math


class Solution:
    def numSquares(self, n: int) -> int:
        ## Approach: Recursion + Memoization
        # Intuition: For each number, we can subtract a perfect square and solve the subproblem for the remainder
        # TC: O(n * sqrt(n)), SC: O(n)

        if int(math.sqrt(n)) ** 2 == n:
            return 1
        
        # Determine all squares < n
        squares = set()
        for i in range(1, n):
            if int(math.sqrt(i)) ** 2 == i:
                squares.add(i)
        
        cache = {}
        def dfs(num):
            if num == 0:
                return 0

            if num in squares:
                return 1
            
            if num in cache:
                return cache[num]
            
            res = math.inf
            for square in squares:
                if square <= num:
                    res = min(res, dfs(num-square))
            
            cache[num] = res + 1
            return cache[num]

        return dfs(n)


