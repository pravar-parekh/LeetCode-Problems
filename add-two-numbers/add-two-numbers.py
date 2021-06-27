# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        params:- 
            l1 : ListNode
                Root node of the first number
            l2 : ListNode
                Root node of the second number
        
        returns:-
            s.next: ListNode
                2 Node of the Answer Linked List
        
        Summary:-
            The program first iterates through list 1, add the two numbers and the carryover
            and mods by 10, to get the units place. The carryOver is updated by dividing the
            previous sum by 10. If list 2 becomes empty then we simply add the remaining
            elements of the linked list to the final sum after accounting for carryover.
            
            Now if the list 1 is exhausted first then fill the rest of the sum with list 2
            elements and then check if any carry over left, if yes than add it.
        
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s = ListNode()
        x = s
        carryOver = 0
        
        while(l1 != None):
            if l2 == None: 
                x.next = ListNode((l1.val + carryOver) % 10, None)
                carryOver = (l1.val + carryOver) // 10
                x = x.next
                l1 = l1.next
            
            else: 
                x.next = ListNode((l1.val + l2.val + carryOver) % 10, None)
                carryOver = (l1.val + l2.val + carryOver) // 10
                x = x.next
                l1 = l1.next
                l2 = l2.next
                
        while(l2 != None):
            x.next = ListNode((l2.val + carryOver) % 10, None)
            carryOver = (l2.val + carryOver) // 10
            x = x.next
            l2 = l2.next
        
        if carryOver != 0:
            x.next = ListNode(carryOver, None)
        return s.next