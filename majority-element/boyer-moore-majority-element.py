'''
    ****Boyer Moore Algorithm****
    
    Summary:-
        We start with the first element choosing it to be candidate. If we number is equal
        to candidate then we add 1 to count. If anything else subtract 1. If count == 0,
        we start again and chose the next element as candidate. To understand this (not
        obvious) look at this example (pipes are inserted to separate runs of nonzero count).
        
        [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
        
        This would make sense as since the majority element occupies more than half spaces,
        the final count will be greater than 0. And this can only be caused by the majority,
        element as for every other element, as they aren't majority there will always be an
        element to make their count 0.
        
        This takes Time: O(N) and Space: O(1)
        
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            count += (1 if num == candidate else -1)
        
        return candidate
