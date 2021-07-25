"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
'''
Summary:-
    First interweave the nodes by creating a true copy of the node and making it the next pointer
    to the original node. Old List: A --> B --> C --> D
                          InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
    
    Once this is done, then set all the random pointers. This is easy as the random pointer of the
    new node would point to the next node of the random pointer of the original node.
    
    Once all random pointers are set, seperate the original and the new nodes.
'''
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if head == None:
            return None
        
        cur = head
        
        while(cur):
            true_next = cur.next
            cur.next = Node(cur.val, true_next)
            cur = true_next
        
        cur = head
        new_head = cur.next
        new_cur = new_head
        
        while(cur.next.next):
            if cur.random:
                new_cur.random = cur.random.next
            else:
                new_cur.random = None
            cur = cur.next.next
            new_cur = new_cur.next.next
        
        if cur.random:
            new_cur.random = cur.random.next
        else:
            new_cur.random = None
        
        cur = head
        new_cur = new_head
        
        while(new_cur.next):
            cur.next = new_cur.next
            new_cur.next = new_cur.next.next
            
            cur = cur.next
            new_cur = new_cur.next
            
        return new_head
        