class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numFull = numBottles
        numEmpty = 0
        currExchange = numExchange
        res = 0

        while numFull > 0 or numEmpty >= currExchange:
            if numEmpty >= currExchange:
                numFull += 1
                numEmpty -= currExchange
                currExchange += 1
            else:
                res += numFull
                numEmpty += numFull
                numFull = 0
        
        return res