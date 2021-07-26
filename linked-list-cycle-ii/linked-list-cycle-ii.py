# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Summary:- 
    Use Floyd Warshall's algorithm (Fast and slow Pointer).
    
    First detect a cycle present or not, using slow and fast pointers. If they become None, then no
    cycle. If they become equal then it means that there is cycle. 
    
    Once its detected, then put the slow pointer to head. And then move slow and fast, only by 1 steps.
    They meet at the start of the cycle.
    
    Explanation here: https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return None
        
        slow = head.next
        fast = head.next.next
        
        while(slow != fast):
            if fast == None or fast.next == None:
                return None

            slow = slow.next
            fast = fast.next.next
        
        slow = head
        while(slow != fast):
            
            fast = fast.next
            slow = slow.next
            
        return slow
