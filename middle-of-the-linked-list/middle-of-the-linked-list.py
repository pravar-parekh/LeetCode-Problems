# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    ****FAST AND SLOW POINTER****
    
    Params:-
        head : ListNode
            Head of the input list.
    
    Returns:-
        ListNode
            The middle node
    
    Summary:-
        We keep a pointer that moves single step at a time and one that moves double steps 
        at a time. When the double step pointer reaches the end, the single step will reach
        the middle.
        
'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        single = head
        double = head
        
        while (double!= None and double.next!= None):
            single = single.next
            double = double.next.next
            
        return single
