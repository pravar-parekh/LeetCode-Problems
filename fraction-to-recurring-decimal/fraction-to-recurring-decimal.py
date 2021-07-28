"""
Summary:-
    First seperate the main part before the decimal, i.e. the quotient. Then, repeat the long division process
    for each remainder, until you find a previously encountered remainder. If encountered then it means quoutients
    will start repeating.
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        quotient, remainder = math.floor(abs(numerator)/abs(denominator)), abs(numerator)%abs(denominator)
        if remainder == 0:
            return str(quotient) if numerator/denominator > 0 else str(abs(quotient) * -1)
        result = str(quotient) + "." if numerator/denominator > 0 else "-" + str(abs(quotient)) + "." 
        
        seen = []
        decimal_quotients = ""
        while(remainder not in seen):
            seen.append(remainder)
            quotient, remainder = math.floor(abs(remainder)*10/abs(denominator)), abs(remainder)*10%abs(denominator)
            decimal_quotients += str(quotient) 
        
        if decimal_quotients[-1] == "0":
            decimal_quotients = decimal_quotients[:len(decimal_quotients) - 1]
            
        if remainder != 0:
            repeat_start = seen.index(remainder)
            decimal_quotients = decimal_quotients[:repeat_start] + "(" + decimal_quotients[repeat_start:]  
            return result + decimal_quotients + ")"
        else:
            return result + decimal_quotients