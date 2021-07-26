# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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