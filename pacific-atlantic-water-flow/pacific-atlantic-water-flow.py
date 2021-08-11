"""
Summary:-
    Use DFS or BFS, Here its DFS. Create two subsets. 1 from pacific ocean and 2 from atlantic.
    Add in the subsets all the elements reachable to the ocean. We can start from the elements
    on the border of the two oceans, then head inside using dfs. If the next element is greater
    than previous element, then its reachable from the previous element. Do this for all border
    elements and we have two sets. Intersection of the two sets is the answer.
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(heights, i, j, subset):
            if (i,j) in subset:
                return
            subset.add((i,j)) 
            # if point on top border            
            if i == 0:
                # top left corner
                if j == 0:
                    if (len(heights) > 1 and heights[i+1][j] >= heights[i][j]):
                        dfs(heights, i+1, j, subset)
                    if (len(heights[0]) > 1 and heights[i][j+1] >= heights[i][j]):
                        dfs(heights, i, j+1, subset)
                    
                # top right corner
                elif j == len(heights[0]) - 1:
                    if (len(heights) > 1 and heights[i+1][j] >= heights[i][j]):
                        dfs(heights, i+1, j, subset)
                    if (len(heights[0]) > 1 and heights[i][j-1] >= heights[i][j]):
                        dfs(heights, i, j-1, subset)
                
                else:
                    if (len(heights) > 1 and heights[i+1][j] >= heights[i][j]):
                        dfs(heights, i+1, j, subset)
                    if (len(heights[0]) > 1 and heights[i][j-1] >= heights[i][j]):
                        dfs(heights, i, j-1, subset)
                    if (len(heights[0]) > 1 and heights[i][j+1] >= heights[i][j]):
                        dfs(heights, i, j+1, subset)
                
            # if point on bottom border
            elif i == len(heights)-1:
                # bottom left corner
                if j == 0:
                    if (len(heights) > 1 and heights[i-1][j] >= heights[i][j]):
                        dfs(heights, i-1, j, subset)
                    if (len(heights[0]) > 1 and heights[i][j+1] >= heights[i][j]):
                        dfs(heights, i, j+1, subset)
                    
                # bottom right corner
                elif j == len(heights[0]) - 1:
                    if (len(heights) > 1 and heights[i-1][j] >= heights[i][j]):
                        dfs(heights, i-1, j, subset)
                    if (len(heights[0]) > 1 and heights[i][j-1] >= heights[i][j]):
                        dfs(heights, i, j-1, subset)
                
                else:
                    if (len(heights) > 1 and heights[i-1][j] >= heights[i][j]):
                        dfs(heights, i-1, j, subset)
                    if (len(heights[0]) > 1 and heights[i][j-1] >= heights[i][j]):
                        dfs(heights, i, j-1, subset)
                    if (len(heights[0]) > 1 and heights[i][j+1] >= heights[i][j]):
                        dfs(heights, i, j+1, subset)
            
            # if point on left border
            elif j == 0:
                if (len(heights) > 1 and heights[i-1][j] >= heights[i][j]):
                    dfs(heights, i-1, j, subset)
                if (len(heights[0]) > 1 and heights[i][j+1] >= heights[i][j]):
                    dfs(heights, i, j+1, subset)
                if (len(heights[0]) > 1 and heights[i+1][j] >= heights[i][j]):
                    dfs(heights, i+1, j, subset)
            
            # if point on right border
            elif j == len(heights[0]) - 1:
                if (len(heights) > 1 and heights[i-1][j] >= heights[i][j]):
                    dfs(heights, i-1, j, subset)
                if (len(heights[0]) > 1 and heights[i][j-1] >= heights[i][j]):
                    dfs(heights, i, j-1, subset)
                if (len(heights) > 1 and heights[i+1][j] >= heights[i][j]):
                    dfs(heights, i+1, j, subset)
            
            # anywhere else       
            else:
                if (len(heights) > 1 and heights[i-1][j] >= heights[i][j]):
                    dfs(heights, i-1, j, subset)
                if (len(heights[0]) > 1 and heights[i][j+1] >= heights[i][j]):
                    dfs(heights, i, j+1, subset)
                if (len(heights) > 1 and heights[i+1][j] >= heights[i][j]):
                    dfs(heights, i+1, j, subset)
                if (len(heights[0]) > 1 and heights[i][j-1] >= heights[i][j]):
                    dfs(heights, i, j-1, subset)
        
        # subset1 for pacific
        subset1 = set()
        # subset2 for atlantic
        subset2 = set()
        
        
        # pacific top row
        for j in range(len(heights[0])):
            dfs(heights, 0, j, subset1)
        
        # pacific left column
        for i in range(len(heights)):
            dfs(heights, i, 0, subset1)
        
        # atlantic right column
        for i in range(len(heights)):
            dfs(heights, i, len(heights[0]) - 1, subset2)
        
        # atlantic bottom row
        for j in range(len(heights[0])):
            dfs(heights, len(heights) - 1, j, subset2)
            
        finalset = subset1.intersection(subset2)
        return list(finalset)