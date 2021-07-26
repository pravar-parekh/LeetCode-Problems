class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = set()
        longest = 0
        current_start = 0
        i = 0
        while(i < len(s)):
            if s[i] in current_substring:
                if len(current_substring) > longest:
                    longest = len(current_substring)
                current_substring = set()
                current_start += 1
                i = current_start
            
            current_substring.add(s[i])
            i += 1
        if len(current_substring) > 0:
            longest = max(longest, len(current_substring))
        return longest
            