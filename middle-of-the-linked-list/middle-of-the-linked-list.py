# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        single = head
        double = head
        
        while (double!= None and double.next!= None):
            single = single.next
            double = double.next.next
            
        return single