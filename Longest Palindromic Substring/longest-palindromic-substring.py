'''
    Summary:-
        To improve over the brute force solution, we first observe how we can avoid unnecessary re-
        computation while validating palindromes. Consider the case "ababa". If we already knew that 
        "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and 
        right end letters are the same.
        
        We define P(i,j) as following:
        P(i,j) = true (if the substring Si, ... , Sj is a palindrome)
        P(i,j) = false (otherwise)
        
        Therefore,
        P(i,j) = (P(i + 1, j - 1) and Si == Sj)
        
        The base cases are:
        P(i,i) = true
        P(i,i+1) = (Si == Si+1)
        
        This yields a straight forward DP solution, which we first initialize the one and two letters 
        palindromes, and work our way up finding all three letters palindromes, and so on...
        
        https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Logical-Thinking
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        start = 0
        length = 1
        table = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        #base case where table[i][i] = true
        for i in range(len(s)):
            table[i][i] = True

        for i in reversed(range(len(s) - 1)): 
            for dist in range(1, len(s) - i):
                j = dist + i
                table[i][j] = s[i] == s[j] if dist == 1 else table[i+1][j-1] and s[i] == s[j]
                if table[i][j]:
                    if dist + 1 > length:
                        start = i
                        length = dist + 1

        return s[start:start + length]
        
        
