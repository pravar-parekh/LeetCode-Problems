class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        
        for word in words:
            length = len(word)
            
            for c in chars:
                if c in word:
                    word = word.replace(c, '', 1)
                if word == "":
                    ans += length
                    break
        
        return ans