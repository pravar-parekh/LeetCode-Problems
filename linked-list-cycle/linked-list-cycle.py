# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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