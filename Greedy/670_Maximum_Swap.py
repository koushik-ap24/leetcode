class Solution:
    def maximumSwap(self, num: int) -> int:
        # Two Pass Solution
        maxArray = [0] * len(str(num))
        # Since str is not mutable, convert to list
        sNum = list(str(num))
        maxArray[-1] = len(sNum) - 1
        
        # Maintain max elements at each position in array (similar to min stack)
        for i in range(len(sNum)-2, -1, -1):
            if int(sNum[i]) > int(sNum[maxArray[i+1]]):
                maxArray[i] = i
            else:
                maxArray[i] = maxArray[i+1]
        
        # Second pass
        for i in range(len(sNum)):
            if sNum[maxArray[i]] > sNum[i]:
                # Swap numbers
                sNum[i], sNum[maxArray[i]] = sNum[maxArray[i]], sNum[i]
                break
        
        print(maxArray)
        # Convert list of char into int
        return int(''.join(sNum))