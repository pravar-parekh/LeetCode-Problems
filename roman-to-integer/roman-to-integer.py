'''
    Params:-
        s : str
            Given Roman Numeral String
        
    Returns:-
        int
            Integer conversion of the Roman Numeral
    
    Summary:-
        Create Dict to store values for each roman numeral. Maintain a variable which tracks
        previous charater we saw. Now go in a reverse order, i.e. units to hundreds etc. Add
        the value of the Roman Literal. But if the previous element and the current element,
        follow the exceptional rule, then subtract instead of adding.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        prev = ''
        ans = 0
        for i in reversed(range(len(s))):
            
            if s[i] == "I" and (prev == "V" or prev == "X"):
                ans -= 1
                
            elif s[i] == "X" and (prev == "L" or prev == "C"):
                ans -= 10
            
            elif s[i] == "C" and (prev == "D" or prev == "M"):
                ans -= 100
            
            else:
                ans+= values[s[i]]
            
            prev = s[i]
            
        return ans