class Solution:
    def mySqrt(self, x: int) -> int:
        ## Important fact: We know the sqrt(x) <= floor(x/2)
        # From this point its binary search!

        if x <= 1:
            return x
        
        left = 1
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            power = mid * mid
            if power == x:
                return mid
            if power < x:
                left = mid + 1
            else:
                right = mid - 1

        return (left + right) // 2
        
