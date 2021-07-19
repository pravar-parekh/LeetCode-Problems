'''
Summary:-
    The O(n) solution with proof by contradiction doesn't look intuitive enough to me. Before moving on,     read any example of the algorithm first if you don't know it yet.

    Here's another way to see what happens in a matrix representation:

    Draw a matrix where rows correspond to the position of the left line, and columns corresponds to the
    position of the right line.

    For example, say n=6. Element at (2,4) would corresponds to the case where the left line is at 
    position 2 and the right line is at position 4. The value of the element is the volume for the case.

    In the figures below, x means we don't need to compute the volume for that case, because:

    on the diagonal, the two lines are overlapped;
    the lower left triangle area of the matrix, the two lines are switched and the case is symmetric to 
    the upper right area.

    We start by computing the volume at (1,6), denoted by o. Now if the left line is shorter than the 
    right line, then moving the right line towards left would only decrease the volume, so all the 
    elements left to (1,6) on the first row have smaller volume. Therefore, we don't need to compute 
    those cases (crossed by ---).

      1 2 3 4 5 6
    1 x ------- o
    2 x x
    3 x x x 
    4 x x x x
    5 x x x x x
    6 x x x x x x
    
    So we can only move the left line towards right to 2 and compute (2,6). Now if the right line is 
    shorter, all cases below (2,6) are eliminated.

      1 2 3 4 5 6
    1 x ------- o
    2 x x       o
    3 x x x     |
    4 x x x x   |
    5 x x x x x |
    6 x x x x x x

    And no matter how this o path goes, we end up only need to find the max value on this path, which   
    contains n-1 cases.

      1 2 3 4 5 6
    1 x ------- o
    2 x x - o o o
    3 x x x o | |
    4 x x x x | |
    5 x x x x x |
    6 x x x x x x
    
    https://leetcode.com/problems/container-with-most-water/discuss/6099/Yet-another-way-to-see-what-happens-in-the-O(n)-algorithm
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        
        l = 0
        r = len(height) - 1
        
        while(l < r):
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]:
                r -= 1
            
            else: l += 1
        
        return max_area
