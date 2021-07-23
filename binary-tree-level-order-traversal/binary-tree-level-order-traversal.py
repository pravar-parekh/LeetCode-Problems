# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Summary:-
    Solve it using queue. traverse the elements in the queue 1 by one. for each traversed, add children
    to the queue. Seperate the levels by adding a value to the queue as a seperator. When seperator 
    encountered, create a new temp list and add the new ones to it. 
'''

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = []
        
        cur = root
        queue.append(cur)
        traversal = [[]]
        level_change = True
        
        while queue:
            cur = queue.pop(0)
            if cur == -10000:
                if not queue:
                    break
                traversal.append([])
                level_change = True
                cur = queue.pop(0)
                
            traversal[-1].append(cur.val)
            if level_change:
                queue.append(-10000)
                level_change = False
                
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        
        return traversal