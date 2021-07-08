'''
    Summary:-
        Store count of letters in a list. For each letter encountered in the second list
        subtract one from the letter count. If all counts are 0 at the end then anagram
        else not an anagram.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = [0] * 26
        
        for i in s:
            count[ord(i) - ord("a")] += 1
        
        for i in t:
            count[ord(i) - ord("a")] -= 1
            
        for i in count:
            if i != 0:
                return False
        
        return True