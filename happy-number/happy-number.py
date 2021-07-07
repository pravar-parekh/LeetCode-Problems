'''
    Summary:-
        Keep a set which tracks all elements that have been seen till now. Then find the sum
        of all the squares of the digits, check if in seen then false else repeat till 1
        encountered then return True.
        
        This is only valid if we can prove that there will be a loop sometime. Or that sum of
        square of digits wont go beyond capacity. 
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while(n != 1):
            n = sum([int(i) ** 2 for i in str(n)])
            if n in seen:
                return False
            seen.add(n)
            
        return True