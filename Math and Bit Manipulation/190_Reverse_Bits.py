class Solution:
    def reverseBits(self, n: int) -> int:
        ## Approach: Take the last bit
        res = 0
        i = 31
        while n:
            bit = n & 1
            res += bit * pow(2, (i))
            n = n >> 1
            i -= 1
        
        return res