from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ## Approach 1: prefix sum
        # Intuition: We can take some cards from the front and some from the back.
        # TC: O(n), SC: O(n)
        n = len(cardPoints)
        prefixSum = [0] * (n+1)
        suffixSum = [0] * (n+1)
        for i in range(n):
            prefixSum[i+1] = (cardPoints[i] + prefixSum[i])
        
        for j in range(n-1, -1, -1):
            suffixSum[j] = cardPoints[j] + suffixSum[j+1]

        res = 0
        for left in range(k+1):
            res = max(res, prefixSum[left] + suffixSum[((n-k)+left)])
        
        return res

        ## Approach 2: Sliding Window
        # Intuition: We can find the minimum sum of a subarray of size n-k and subtract it from the total sum.
        # TC: O(n), SC: O(1)
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total

        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            res = max(res, total)
            l += 1
            r += 1

        return res