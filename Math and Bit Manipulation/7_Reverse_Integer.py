class Solution:
    def reverse(self, x: int) -> int:
        ## Approach 1 -> bruteforce
        # Isolate each digit from the number via mod operations
        # Store digits in a list
        # Reverse the digit and apply the current place position
        digits = []
        num = abs(x)
        power = 1
        while num > 0:
            place = pow(10,power)
            digits.append(num % place)
            num = int(num/place) * place
            power += 1
        

        for i in range(len(digits)):
            digits[i] = int(digits[i] / pow(10,i))
            power += 1
    
        res = 0
        place = len(digits)-1
        for digit in digits:
            res += digit * pow(10, place)
            place -= 1
        
        if (res > pow(2,31)-1) or res < -(pow(2,31)):
            return 0
        
        if x < 0:
            return -res
        
        return res

        ## Approach 2: One pass solution
        # Extract digit from last to front
        # At each pass, check if res > max value
        # Edit the res in place
        res = 0
        num = abs(x)
        while num:
            digit = num % 10
            num = num // 10

            # Check for overflow
            if res > (2**31 - 1) // 10:
                return 0
            
            res = res * 10 + digit
        
        return res if x > 0 else -res
