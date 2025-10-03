class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numEmpty = 0
        numFull = numBottles
        res = 0

        while numFull > 0 or numEmpty + numFull >= numExchange:
            if numFull > 0:
                res += numFull
                numEmpty += numFull
                numFull = 0
            else:
                numFull = numEmpty // numExchange
                numEmpty = numEmpty % numExchange
        
        return res
        