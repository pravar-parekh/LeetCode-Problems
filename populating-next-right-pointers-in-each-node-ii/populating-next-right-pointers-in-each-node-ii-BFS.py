"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
'''
Summary:- 
    ##### BFS METHOD #####
    
    Use queue, add a seperator for each new level. Then for each same level fill out the next pointer of
    the nodes. This traverses the tree in BFS manner.
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        level_change = True

        while queue:
            cur = queue.pop(0)
            if cur == 1000:
                if queue == []:
                    break
                level_change = True
                cur = queue.pop(0)
                
            if queue and queue[0] != 1000:
                cur.next = queue[0]
                
            if level_change:
                queue.append(1000)
                level_change = False
            if cur.left: 
                queue.append(cur.left)
            if cur.right: 
                queue.append(cur.right)
            
        return root
        
