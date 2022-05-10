class Solution(object):
    def divide(self, dividend, divisor):
        # Avoids overflow when converting to positive (can't store 2147483648)
        if divisor == -2147483648 and dividend != divisor:
            return 0
        
        # Turn dividend and divisor into positive numbers and calculate if the result will be negative
        negativeResult = False
        if dividend < 0:
            dividend -= dividend + dividend
            negativeResult = not negativeResult
        
        if  divisor < 0:
            divisor -= divisor + divisor
            negativeResult = not negativeResult
        
        
        if dividend < divisor:
            return 0
        
        # Calculate resulte
        q = 0
        r = dividend
        while True:
            if r >= divisor:
                m = 1
                nextV = divisor
                while True:
                    if r >= nextV << 1:
                        m <<= 1
                        nextV <<= 1
                    else:
                        q += m
                        r -= nextV
                        break
                
            if r < divisor:
                if (negativeResult):
                    q -= q + q
                
                return min(max(-2147483648, q), 2147483647)