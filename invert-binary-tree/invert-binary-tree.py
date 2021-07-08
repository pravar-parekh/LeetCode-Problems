# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    Summary:-
        Use recursion for this. This would make the function act as DFS and reach the bottom
        nodes and reverse from there. If root reaches none then return root. Else root.left 
        would be equal to invertTree(root.right) and root.right would be equal to 
        invertTree(root.left) return root at the end.
'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        
        return root
        