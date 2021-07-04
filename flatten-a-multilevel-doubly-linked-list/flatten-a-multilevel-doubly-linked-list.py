"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
'''
    Params:-
        head : Node
            Head of the given list
        
    Returns:-
        Node
            Head of the final list
    
    Summary:-
        We move through the entire list sequentially. When we encounter a child at node x,
        we then move through the entire list of the child and reach it's last node. we then
        connect the last node to x.next, and then connect the x.child to x. Then we proceed
        to the next element.
'''
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        x = head
        
        while(x!= None):
            
            if x.child == None:
                x = x.next
            
            else: 
                temp = x.child
                while(temp.next != None):
                    temp = temp.next
                    
                temp.next = x.next
                if x.next != None:
                    x.next.prev = temp
                
                x.next = x.child
                x.child.prev = x
                x.child = None
            
        return head