# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
    Params:- 
        headA : ListNode
            Head of the list A
        
        headB : ListNode
            Head of the list B
    
    Returns:-
        ListNode
            The node at which intersection happens or None
    
    Summary:-
        We take two pointers and iterate through both the list in a loop which ends if 
        they are equal. Since the lengths of both lists could be different, one could reach
        end before the other. When that happens we simply set the pointer to the Head of the
        other list. This will also occur with the pointer of the other list. But when the
        second pointer is changed to the head of the first list, the other pointer would
        already be ahead by the difference of their lengths in the shorter list. Thus they now
        should meet at the intersection or reach Ends together, thus ending the loop. Dry run
        this to further understand.
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        a = headA
        b = headB
        
        while a!=b: 
            if a == None:
                a = headB
            else:
                a = a.next
            
            if b == None:
                b = headA
            else: 
                b = b.next
            
        return a
