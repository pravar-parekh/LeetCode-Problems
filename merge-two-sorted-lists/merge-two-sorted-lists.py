# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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