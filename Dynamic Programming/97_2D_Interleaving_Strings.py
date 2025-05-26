## Bottom up solution - start from end of s3 and work backwards
## Hardest 2D DP problem so far :(

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < n and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
