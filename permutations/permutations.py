'''
Summary:- 
    https://leetcode.com/problems/permutations/discuss/685868/DFSbacktracking-PythonJavaJavascript-PICTURE
    
    Classic combinatorial search problem, we can solve it using 3-step system

    Identify states
        What state do we need to know whether we have reached a solution (and using it to construct a 
        solution if the problem asks for it).
        We need a state to keep track of the list of letters we have chosen for the current permutation
    
    What state do we need to decide which child nodes should be visited next and which ones should be 
    pruned?
    We have to know what are the letters left that we can still use (since each letter can only be used 
    once).

    Draw the State-space Tree
                                   [ ]
                    [1]            [2]            [3]
                [1,2][1,3]     [2,1][2,3]     [3,1][3,2]
              [1,2,3][1,3,2] [2,1,3][2,3,1] [3,1,2][3,2,1]  
              
    DFS on the State-space tree
        Using the backtracking template as basis, we add the two states we identified in step 1:
        
    A list to represent permutation constructed so far, path
    A list to record which letters are already used, used, used[i] == true means ith letter in the origin
    list has been used.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(path, seen, result):
            
            if len(path) == len(nums):
                result.append(path[:])  # note [:] make a deep copy since otherwise we'd be append the same list over and over
                return
        
            for i, num in enumerate(nums):
                # skipped seens nums
                if seen[i]:
                    continue
                
                # add number to path, mark as seen
                path.append(num)
                seen[i] = True
                dfs(path, seen, result)
                
                path.pop()
                seen[i] = False
                
        
        result = []
        dfs([], [False] * len(nums), result)
        
        return result