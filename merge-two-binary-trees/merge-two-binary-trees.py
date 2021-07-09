# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    Summary:-
        Simple Recursive function. If either root is None, return the other one. If both aren't
        None, then add the value of both of them into the root1 (Merging root2 into root1). Then
        left of the root1 would be merging left subtree of both trees, and right will be merging
        right subtree of both the trees. return root1 at the end.
'''
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None:
            return root2
        
        if root2 == None:
            return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1