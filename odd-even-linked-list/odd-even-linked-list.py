# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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