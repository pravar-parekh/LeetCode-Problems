# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Summary:- 
    First, travel down the bigger tree via standard dfs, if we find node equal to the value of root of the smaller tree, compare the subtrees.
    We travel down both subtrees at the same time and if and only if every node is the same then we know we have found the right subtree.
'''
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        if not root:
            return False
        
        elif self.isSameTree(root, subRoot):
            return True
        
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        if root and subRoot:
            return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        
        return root is subRoot
    

        