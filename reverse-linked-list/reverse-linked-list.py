# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    ****ITERATIVE APPROACH****
    
    Params:- 
        head : ListNode
            Head of the input list
        
    Returns:-
        ListNode
            New head of the list
    
    Summary:-
        Moves iteratively throughout the original list till None is reached. Changes 
        next of the current element to previous element, changes previous element to
        to the current element and changes the current element to the next element which
        was stored temporarily. Returns the previous element at the end. 
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        current = head
        
        while (current != None):
            nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
        
        return prev
        