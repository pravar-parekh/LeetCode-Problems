class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        new_i = n - 1 - k
        
        nums[:] = nums[new_i + 1:] + nums[:new_i+1]
    