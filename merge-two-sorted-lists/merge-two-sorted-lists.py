# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    Iterative Solution:
    
    Params:-
        l1 : ListNode
            Head of List 1
        l2 : ListNode
            Head of List 2
    
    Returns:-
        head : ListNode
            Head of the Solution List
    
    Summary:-
        If the l1 or l2 is empty return the other one. We set the head of our solution to
        the element which is lesser between the heads of both the lists. Then iteratively
        check if l1 < l2 or vice versa. Insert its pointer to the solution list and move
        the solution and the chosen list to its next element. Once we reach the end of
        either lists l1 or l2, we simply put the next pointer of the list which hasn't been
        completed to the solution list and return the head.
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        
        else: 
            head = l2
            l2 = l2.next
        x = head    
        while (l1 != None and l2 != None):
            
            if l1.val < l2.val:
                x.next = l1
                l1 = l1.next
            
            else: 
                x.next = l2
                l2 = l2.next
            
            x = x.next
                
            
        if l1 != None:
            x.next = l1
        elif l2 != None:
            x.next = l2
            
        return head
