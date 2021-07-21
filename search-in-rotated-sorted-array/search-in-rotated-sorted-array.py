'''
Summary:-
    We have an ascending array, which is rotated at some pivot.
    Let's call the rotation the inflection point. (IP)
    One characteristic the inflection point holds is: arr[IP] > arr[IP + 1] and arr[IP] > arr[IP - 1]
    So if we had an array like: [7, 8, 9, 0, 1, 2, 3, 4] the inflection point, IP would be the number 9.

    One thing we can see is that values until the IP are ascending. And values from IP + 1 until end are also ascending 
    (binary search).
    Also the values from [0, IP] are always bigger than [IP + 1, n].

    intuition:
    We can perform a Binary Search.
    If A[mid] is bigger than A[left] we know the inflection point will be to the right of us, meaning values from 
    a[left]...a[mid] are ascending.

    So if target is between that range we just cut our search space to the left.
    Otherwise go right.

    The other condition is that A[mid] is not bigger than A[left] meaning a[mid]...a[right] is ascending.
    In the same manner we can check if target is in that range and cut the search space correspondingly.

    Time complexity: O(logn)
    Space complexity: O(1)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        if len(nums) == 0:
            return -1
        
        while(l<=r):
            m = l - (l - r)//2
            if target == nums[m]:
                return m
            
            # inflection point to the right. Left is strictly increasing
            if nums[l] < nums[m]:
                
                if nums[l] <= target < nums[m]:
                    r = m - 1
                
                else:
                    l = m + 1
            
            # inflection point to the left of me. Right is strictly increasing
            else:
                
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                
        return -1