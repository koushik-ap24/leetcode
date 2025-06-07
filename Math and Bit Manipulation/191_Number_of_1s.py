class Solution:
    def hammingWeight(self, n: int) -> int:
        ## Approach 1:
        # Right shift and bitmask with 1 until number becomes 0
        # This will iterate through all bits in the number
        mask = 1
        res = 0
        while n:
            res += (n & mask)
            n = n >> 1
        
        return res

        ## Approach 2:
        # bitmask with n-1 until n is 0
        # This will only run for as many 1s in the number
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        
        return n