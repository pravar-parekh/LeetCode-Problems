"""
Summary:- 
    Iterate through each of the cell and if it is an island, do dfs to mark all adjacent islands, then increase 
    the counter by 1.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    
                    count += 1
        
        return count
                
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        
        grid[i][j] = "0"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        return