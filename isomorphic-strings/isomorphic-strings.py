'''
    Summary:-
        Iterate through the s string. As we come across values, check if they are in the 
        equivalence dictionary. If yes then check if corresponding t string value matches,
        the equivalence dictionary value. If not present in the dictionary, then add to the
        dictionary. 
        
        If loop reaches end then it means isomorphic. So return True.
'''
class Solution:
    
    def __init__(self):
        self.equivalent = dict()
        
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        for i in range(len(s)):
            
            if s[i] in self.equivalent:
                if t[i] != self.equivalent[s[i]]:
                    return False
            
            elif t[i] in self.equivalent.values():
                if s[i] != self.get_key(t[i]):
                    return False
            else:
                self.equivalent[s[i]] = t[i]

        return True

    def get_key(self, val):
        for key, value in self.equivalent.items():
            if val == value:
                 return key
        return None