'''
    Summary:- 
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            nums[temp] = -abs(nums[temp])
            
        return [i+1 for i,v in enumerate(nums) if v >= 0]