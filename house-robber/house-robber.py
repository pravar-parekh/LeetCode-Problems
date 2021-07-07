'''
    Params:-
        nums: List[int]
            Array of numbers (profits from houses)
            
    Returns:-
        int
            Max Profit possible
            
    Summary:-
        This is a DP problem. For explanation check this: 
        https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        prev1 = 0
        prev2 = 0
        
        for num in nums:
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp
            
        return prev1