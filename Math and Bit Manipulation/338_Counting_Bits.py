from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ## Approach 1 -> division
        # TC: O(nlog(n)), SC: O(1) [excluding result array]
        # res = []
        # for i in range(n+1):
        #     count = 0
        #     num = i
        #     while num:
        #         count += num & 1
        #         num = num >> 1
        #     res.append(count)
        
        # return res

        ## Approach 2 -> Dynamic Programming
        # TC: O(n), SC: O(1) [excluding result array]
        dp = [0] * (n+1)
        power = 0
        for i in range(1, n+1):
          # Check if number if power of 2 using below trick.
            if i & (i-1) == 0:
                power = i
            
            dp[i] = 1 + dp[i-power]
        
        return dp
