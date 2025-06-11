class Solution:
    def getSum(self, a: int, b: int) -> int:
        ## Approach: Only for positive integers solution
        carry = 0
        res = 0
        shift = 0
        while a or b or carry:
            aBit = a & 1
            bBit = b & 1
            add = (aBit ^ bBit)
            newBit = carry ^ aBit ^ bBit
            carry = (aBit & bBit) | (carry & add)
            newBit = newBit << shift
            res = res | newBit
            shift += 1
            a = a >> 1
            b = b >> 1
        
        return res
    
        ## Approach2: Address negative integers
        # Turns our python is not great with bit manipulation for negative integers
        # So we can use Java instead to solve this problem

