class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums, 0, len(nums)-2), self.rob_helper(nums, 1, len(nums)-1))

    def rob_helper(self, nums: List[int], start: int, end: int) -> int:
        print(start)
        prev1 = nums[start]
        prev2 = 0
        
        for i in range(start+1, end+1):
            if prev1 > prev2 + nums[i]:
                current = prev1
            else:
                current = prev2 + nums[i]
                
            prev2, prev1 = prev1, current
            
        return prev1
            