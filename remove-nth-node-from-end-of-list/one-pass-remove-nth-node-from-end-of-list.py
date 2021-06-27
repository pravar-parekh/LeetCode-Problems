# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
    **** ONE PASS SOLUTION ****
    Params:- 
        head : ListNode
            Head of the Linked List
            
        n : int
            The nth number index to remove from the end of the linked list
            
    Returns:-
        dummy.next : Listnode
            Head of the linked list
    
    Summary :-
        The One-Pass solution maintains 2 points x1 and x2. x1 first moves by n in the list.
        Then x2 and x1 both start moving till x1 reaches the end. This makes x2 reach the
        element we need to delete i.e. total elements - n. x3 maintains pointer to the element
        previous to x2 so we can change it's next to skip x2. Dummy is created to handle a case
        where the head is removed or only 1 element.
'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        x1 = dummy
        x2 = head
        x3 = dummy
        count = 0

        while (count < n):
            count += 1
            x1 = x1.next   
        
        while (x1.next != None):
            x3 = x2
            x2 = x2.next
            x1 = x1.next
        
        x3.next = x2.next  
        
        return dummy.next
