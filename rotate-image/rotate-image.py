'''
Summary:- 
    The most elegant solution for rotating the matrix is to firstly reverse the matrix around the main 
    diagonal, and then reverse it from left to right. These operations are called transpose and reflect 
    in linear algebra.
    
    Even though this approach does twice as many reads and writes as approach 1, most people would 
    consider it a better approach because the code is simpler, and it is built with standard matrix 
    operations that can be found in any matrix library.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Reverse rows
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][len(matrix)-1 - j] =  matrix[i][len(matrix)-1 - j], matrix[i][j]
        
        