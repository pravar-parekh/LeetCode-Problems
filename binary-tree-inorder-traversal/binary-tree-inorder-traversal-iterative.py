# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Summary:-
    Iterative Approach
'''
class Solution: 
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        if (root == None):
            return traversal
        
        stack = []
        done_reading = []
        stack.append(root)
        cur = root
        while(stack):
            
            if cur.left and cur.left not in done_reading:
                stack.append(cur.left)
                cur = cur.left
                continue
            
            cur = stack.pop()
            traversal.append(cur.val)
            done_reading.append(cur)
            
            if cur.right and cur.right not in done_reading:
                stack.append(cur.right)
                cur = cur.right
                continue
        
        return traversal
        
