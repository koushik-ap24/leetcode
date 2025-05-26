class Solution:
    # Got the recursion intuition, Needed hint to come up with base case
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        # Top-Down = Just cache the recursive call results
        cache = {}

        def dfs(i, j):
            # if reached end of word1, then return the remaining chars length in word2 for insertion
            if i == n:
                return len(word2[j:m])
            # if reached end of word2, then return the remaining chars length in word1 for deletion
            if j == m:
                return len(word1[i:n])
            if (i,j) in cache:
                return cache[(i,j)]

            if word1[i] == word2[j]:
                cache[(i,j)] = dfs(i+1, j+1)
            else:
                # insertion, replace, and deletion in that order
                cache[(i,j)] = 1 + min(dfs(i, j+1), dfs(i+1, j+1), dfs(i+1, j))
        
            return cache[(i,j)]
        
        return dfs(0,0)