# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    **** TWO PASS SOLUTION ****
    Params:- 
        head : ListNode
            Head of the Linked List
            
        n : int
            The nth number index to remove from the end of the linked list
            
    Returns:-
        dummy.next : Listnode
            Head of the linked list
    
    Summary :-
        The TWO-Pass solution first goes through the entire list to find total number elements.
        Then it calculates n_ the position of the element to remove. It moves to the element previous
        to n_ element and changes its next to skip the n_ element. If element head is removed then it 
        simply returns head.next or if only 1 element then it returns None.          
'''

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        total = 0
        x = head
        while(x!= None):
            total += 1
            x = x.next
        
        x = head
        n_ = total - n
        
        count = 0
        
        if total == 1:
            return None
        
        if n_ == 0:
            return head.next
        
        while(count != n_ - 1):
            count += 1
            x = x.next
            
        x.next = x.next.next
        
        return head
