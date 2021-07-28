"""
Summary:-
    Split the string into a list on spaces. Reverse the list, and then return the joined list as a string
    seperated by " ".
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()
        for i in range(len(s)//2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i] 
        return " ".join(s)
            
                
        
            