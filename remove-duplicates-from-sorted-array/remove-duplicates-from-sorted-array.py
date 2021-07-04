'''
    ****TWO POINTER APPROACH****
    
    Params:- 
        nums : List[int]
            Given sorted array of integers
    
    Returns:-
        int
            The last index of the solution array to be counted
    
    Summary:-
        We keep track of two pointers to the array. One that checks if duplicate. If it matches
        the current element i.e. it is a duplicate we just increment the pointer. Else, we then
        replace the element on the replacePointer with element on the checkPointer. This shifts
        the non duplicate elements to their final place.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return None
        replacePointer = 1
        checkPointer = 1
        current = nums[0] 
        while (checkPointer < len(nums)):
            
            if nums[checkPointer] == current:
                checkPointer += 1
            
            else:
                nums[replacePointer] = nums[checkPointer] 
                current = nums[replacePointer]
                replacePointer += 1
                checkPointer += 1
        
        return replacePointer