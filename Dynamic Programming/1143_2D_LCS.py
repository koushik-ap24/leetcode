class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Base cases: dp[i][0] = 0 and dp[0][j] = 0
        # Consider when either str is empty

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]