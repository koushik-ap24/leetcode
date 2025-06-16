from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valRight = valLeft = 0
        for i in range(len(flowerbed)):
            if not n:
                print(flowerbed)
                return True

            if flowerbed[i] == 0:
                valRight = flowerbed[i+1] if i+1 < len(flowerbed) else 0
                if valRight == valLeft == 0:
                    flowerbed[i] = 1
                    n -= 1
                
            valLeft = flowerbed[i]
        
        return n == 0