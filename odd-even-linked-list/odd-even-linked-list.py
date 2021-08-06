# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Summary:- 
    We only need to save which one would the first even indexed node. So that when we reach the
    end of the odd nodes, we can attach the even head to it. After that we only next to reassign
    all the next pointers to alternate pointers until we reach the end, at which we attach the
    two lists.

"""
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        first_eve = head.next
        
        cur_odd = head
        cur_eve = first_eve
        
        while cur_odd.next and cur_eve.next:
            cur_odd.next, cur_eve.next = cur_odd.next.next, cur_eve.next.next
            
            cur_odd, cur_eve = cur_odd.next, cur_eve.next
            
        cur_odd.next = first_eve
        
        return head
