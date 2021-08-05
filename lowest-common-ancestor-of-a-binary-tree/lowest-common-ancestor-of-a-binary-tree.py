# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Summary:- 
    Start traversing the tree from the root node.
    
    If the current node itself is one of p or q, we would mark a variable mid as True and 
    continue the search for the other node in the left and right branches.
    
    If either of the left or the right branch returns True, this means one of the two nodes was 
    found below.
    
    If at any point in the traversal, any two of the three flags left, right or mid become True, 
    this means we have found the lowest common ancestor for the nodes p and q.
"""

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
        
