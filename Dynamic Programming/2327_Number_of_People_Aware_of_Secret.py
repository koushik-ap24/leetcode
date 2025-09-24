class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        ## Approach: Dynamic Programming
        ## Intuition: On each day, we can keep track of how many new people learn the secret
        ## and how many people are eligible to share the secret
        ## A person who learns the secret on day i can start sharing it on day i + delay
        ## and forgets it on day i + forget
        # TC: O(n), SC: O(n)
        dp = [0] * (n+1)
        dp[1] = 1
        MOD = 10 ** 9 + 7

        ## dp keeps track of how many new people learn secret in day i
        ## total_knowers tracks how many people are eligible to share on a given day
        ## Since each eligible person shares to one new person, dp[i] = total_knowers
        total_knowers = 0
        for i in range(2, n+1):
            if i - delay > 0:
                total_knowers = (total_knowers + dp[i - delay]) % MOD
            
            if i - forget > 0:
                total_knowers = (total_knowers - dp[i-forget] + MOD) % MOD
            
            dp[i] = total_knowers

        res = 0
        for i in range(n- forget + 1, n+1):
            res = (res + dp[i]) % MOD
        
        return res

        