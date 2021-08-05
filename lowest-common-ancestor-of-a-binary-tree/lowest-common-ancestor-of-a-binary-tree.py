# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recurse_tree(cur: 'Treenode') -> int:
            
            if not cur:
                return 0
            
            # left
            left = recurse_tree(cur.left)
            
            # right
            right = recurse_tree(cur.right)
            
            # current node i.e. middle
            
            mid = 1 if cur == p or cur == q else 0
            
            if mid + right + left >= 2:
                self.ans = cur
                
            return mid or left or right
        
        # Traversing the tree
        recurse_tree(root)
        return self.ans
        