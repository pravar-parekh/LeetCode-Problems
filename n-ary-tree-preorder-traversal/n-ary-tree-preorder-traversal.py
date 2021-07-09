"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.lis = []
        
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if root == None:
            return []
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            
            for child in reversed(node.children):
                stack.append(child)
                
        return ans
            