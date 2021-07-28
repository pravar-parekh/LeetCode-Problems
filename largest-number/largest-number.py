"""
Summary:-
    we simply need to change how the integers are compared when sorting. Normaly we check wether a>b
    but here we need to check which concatenation would be bigger. i.e. a+b or b+a. For the rest of 
    steps apply simple sort.
"""

class Solution:

    def compare(self, num1, num2):
        return str(num1) + str(num2) > str(num2) + str(num1)
     
    def largestNumber(self, nums: List[int]) -> str:
        self.quick_sort(nums, 0, len(nums) - 1)
        if nums[0] != 0: 
                return "".join(map(str,nums)) 
        else: return "0"
        
    def quick_sort(self, nums, l, r):
        if l >= r:
            return
        
        pos = self.partition(nums, l, r)
        self.quick_sort(nums, l, pos-1)
        self.quick_sort(nums, pos+1, r)
        
    def partition(self, nums, l, r):
        low = l
        
        while(l<r):
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
                
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low