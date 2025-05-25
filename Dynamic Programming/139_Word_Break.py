from typing import List


## To consider to put a space, we need to check if any previous place is valid, and if the substring from that space to the current space is valid
## If any space before the current one is true, then we can mark this as true as we have found atleast 1 valid split.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordSet = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]