# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.traversal = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if (root == None):
            return self.traversal
        
        self.inorderTraversal(root.left)
        self.traversal.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.traversal
        