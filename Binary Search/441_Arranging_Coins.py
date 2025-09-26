import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Binary search using arithmetic series formula
        left = 1
        right = max(1,int(math.ceil(n/2)))
        res = 1

        while left <= right:
            mid = (left+right)//2
            if ((1+mid)/2)*mid > n:
                right = mid - 1
            else:
                left = mid + 1
                res = max(res, mid)
                 
        return res