import math
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        ## Approach:
        # Both players are playing optimally
        # At each level, return Alice's score
        # If its Alice's turn, we want the max, otherwise we want the min as Bob is trying to minimise Alice's score
        # The end result will be the max score for Alice since she goes first

        cache = {}
        
        def dfs(player,i,M):
            if i == len(piles):
                return 0
            
            if (player,i,M) in cache:
                return cache[(player,i,M)]
            
            res = 0 if player == 0 else math.inf
            total = 0 # prefix sum for all piles before 2M
            for X in range(1, 2*M+1): # 1 <= X <= 2M
                if i + X > len(piles):
                    break
                total += piles[i + X - 1]
                if player == 0: # Alice
                    res = max(res, total + dfs(1, i+X, max(M,X)))
                else:
                    # Since its not Bob's score, he just wants to minimise Alice's score
                    # So no need to add total to recursive call result
                    res = min(res, dfs(0, i+X, max(M,X)))
            cache[(player,i,M)] = res
            return res
        
        return dfs(0,0,1)

        # TC: O(n^3), SC: O(n^2)