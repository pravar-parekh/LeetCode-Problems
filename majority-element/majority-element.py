'''
    ****Hash Table Method****
    
    Summary:-
        Store the count for each number in a hashtable. Then return the number for which
        count > half.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = dict()
        
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            
            else:
                hashtable[i] += 1
        
        half = len(nums)/2
        for number in hashtable:
            if hashtable[number] > half:
                return number
