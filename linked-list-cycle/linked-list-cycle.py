# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
    ****Tortoise and Hare Method****
    Params:-
        head : ListNode
            Head of the list
    
    Returns:-
        Bool
            True if List has cycle else false
    
    Summary:- 
        Use the Tortoise and Hare algorithm, i.e. a fast and a slow pointer. Fast moves
        2x the speed of the slow pointer. If the two ever meet before the fast reaches
        None, then it has cycle else no cycle.
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        flag = False
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                flag = True
                break
        
        return flag
