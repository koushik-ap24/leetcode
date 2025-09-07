class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Brute force
        # ans = 1
        # x = x if n >= 0 else 1/x
        # for _ in range(abs(n)):
        #     ans *= x
        
        # return ans

        # Optimal - recursion
        # Notice that x^n = x^(n/2)^2 (square half the power)
        # You can keep doing this until power reaches 1 or 0, which is base case
        # TC: O(logn), SC: O(logn)
        def recurse(n):
            if n == 0:
                return 1

            if n == 1:
                return x
            
            if n % 2 == 0:
                val = recurse(n/2)
                return val * val
            
            val = recurse((n-1)/2)
            return x * val * val
        
        res = recurse(abs(n))
        return res if n >= 0 else 1/res