# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head
        
        if head.next == None:
            return head        
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        head = head.next
        
        while(cur.next and cur.next.next):
            first = cur.next
            second = cur.next.next
            
            cur.next = second
            first.next = second.next
            cur.next.next = first
            
            cur = cur.next.next
            
        return head