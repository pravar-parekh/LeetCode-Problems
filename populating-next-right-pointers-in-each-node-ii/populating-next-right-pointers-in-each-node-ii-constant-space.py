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
    ##### CONSTANT SPACE BFS METHOD #####
    
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37824/AC-Python-O(1)-space-solution-12-lines-and-easy-to-understand
    
    The algorithm is a BFS or level order traversal. We go through the tree level by level. node is the 
    pointer in the parent level, tail is the tail pointer in the child level.
    The parent level can be view as a singly linked list or queue, which we can traversal easily with a 
    pointer.
    Connect the tail with every one of the possible nodes in child level, update it only if the connected 
    node is not nil.
    Do this one level by one level. The whole thing is quite straightforward.
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        tail = dummy = Node(0)
        node = root
        while(node):
            tail.next = node.left
            if tail.next:
                tail = tail.next
            
            tail.next = node.right
            if tail.next:
                tail = tail.next
                
            node = node.next
            
            if not node:
                tail = dummy
                node = tail.next
            
        return root
        
