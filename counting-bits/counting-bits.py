"""
Summary:-
    For each binary number, if we multiply by 2, we just add a 0 at the end. Any next number
    would be adding a 1 at the end. Thus any number would then have the same number of 1's as 
    the number divided by 2 and if its an odd number then it would be the number divided by 2 
    plus 1. 
    
    Since i>>1 is faster than i//2 and does the same thing, thats an optimization.
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n+1)]
        
        for i in range(1, n+1):
            ans[i] = ans[i>>1] + i%2    #### i>>1 does the same thing as i//2
            
        return ans