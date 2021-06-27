# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        total = 0
        x = head
        while(x!= None):
            total += 1
            x = x.next
        
        x = head
        n_ = total - n
        
        count = 0
        
        if total == 1:
            return None
        
        if n_ == 0:
            return head.next
        
        while(count != n_ - 1):
            count += 1
            x = x.next
            
        x.next = x.next.next
        
        return head