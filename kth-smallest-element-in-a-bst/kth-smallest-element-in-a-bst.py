# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Summary:
    Just do inorder traversal. Count the number of nodes, till the kth node is reached and return the node
"""

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return root
        
        count = 0
        node = root
        
        stack = [root]
        while(count < k):
            if node:
                stack.append(node)
                node = node.left
            
            elif stack:
                node = stack.pop()
                count += 1
                if count == k:
                    break

                node = node.right
            
            else:
                break
                
        return node.val