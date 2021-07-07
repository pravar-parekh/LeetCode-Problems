'''
    Params:-
        nums : List[int]
            Array of Integers
        k : int
            Rotate the array by k
            
    Summary:-
        Create a new k which is mod of n. This removes the possibility of cycling i.e. complete
        360 rotation. Find the spot of the new first number by subtracting k from total length
        of the array. Then split and replace the new array.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        new_i = n - 1 - k
        
        nums[:] = nums[new_i + 1:] + nums[:new_i+1]
