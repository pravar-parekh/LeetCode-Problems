'''
    Params:-
        nums : List[int]
            Array of 1's and 0's
        
    Returns:-
        int
            maximum number of consecutive 1's
    
    Summary:-
        Iterate through the array, add 1 to the count if 1 encountered. If 0 encountered,
        then set max_ = maximum of count and max_. Return maximum of max_ and final count.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ = 0
        
        for i in nums:
            if i == 0:
                max_ = max(count, max_)
                count = 0
            else:
                count += 1
        
        return max(count, max_)