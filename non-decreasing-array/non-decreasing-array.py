'''
    Summary:- Well, I use count to remember how many descending pairs in the array, if count>=2, obviously we cannot 
    modify a single element to obtain a non-descreaing array, so we return False. When count equals one, we check if we 
    can modify nums[i] (the first one in the descending pair, by decreasing it) or nums[i+1] (the second one in the 
    descending pair, by increasing it), if in both situations, we cannot, then we will also return False. In this way, the 
    situation that return False is complete, the others will return True. And also in this way, we can return much earlie
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count+=1
                
            if count > 1 or ((i-1>=0 and nums[i-1] > nums[i+1]) and (i+2<len(nums) and nums[i] > nums[i+2])):
                return False
        
        return True