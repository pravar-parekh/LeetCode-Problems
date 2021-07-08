class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        string = ''
        for i in range(len(words)):
            words[i] = words[i][::-1]
            if (i == len(words) - 1):
                string += words[i]
            else:
                string += words[i] + " "
        
        return string