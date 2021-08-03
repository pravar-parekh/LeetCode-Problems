"""
Summary:-
    Backtracking problem. Used dfs. for each number in range 1-9 start with each number. if k and n both become 
    0 together, means we found the ans, so we add the path taken to the answer list.
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(list(range(1,10)), k, n, [], ans)
        return ans
    
    def dfs(self, nums, k, n, path, ans):
        if k<0 or n<0:
            return
        if k==0 and n==0:
            ans.append(path)
        
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ans)