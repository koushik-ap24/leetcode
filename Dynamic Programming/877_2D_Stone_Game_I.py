from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(l,r):
            if l > r:
                return 0
            
            if (l,r) in cache:
                return cache[(l,r)]
            
            # Check if Alice turn, which is when subarray has even elements
            # Otherwise its Bob's turn, in which case you dont add to Alice's total (essentially skip this turn)
            turn = (r-l) // 2
            left = piles[l] if turn else 0
            right = piles[r] if turn else 0
            cache[(l,r)] = max(dfs(l+1, r) + left, dfs(l,r-1) + right)
            return cache[(l,r)]

        # Return true only if max stones for Alice exceeds the remaining stones (which Bob will pick)
        total = sum(piles)
        Alice = dfs(0,(len(piles)-1))
        return Alice > total-Alice