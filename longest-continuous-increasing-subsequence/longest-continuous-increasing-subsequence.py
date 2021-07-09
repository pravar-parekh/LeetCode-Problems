class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max_ = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
                max_ = max(count, max_)
                
            else:
                count = 1
                
        return max_