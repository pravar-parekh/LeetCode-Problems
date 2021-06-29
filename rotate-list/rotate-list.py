# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head == None:
            return None
        x = head
        total = 1
        while (x.next != None):
            total += 1
            x = x.next
        
        k = k%total
        new_total = 0
        k_ = -1
        while (k_ < 0):
            new_total += total
            k_ = new_total - k
        
        if k_ == 0:
            return head
        
        x.next = head
        x = head
        new_total = 0
        
            
        # k_ = total - k
        count = 1
        while (count < k_):
            print(count)
            count += 1
            x = x.next
            
        head_new = x.next
        x.next = None
            
        return head_new
        