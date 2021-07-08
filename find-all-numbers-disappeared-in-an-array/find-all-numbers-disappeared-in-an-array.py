class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        notPresent = []
        
        for i in range(1, len(nums)+1):
            if i not in numSet:
                notPresent.append(i)
                
        return notPresent