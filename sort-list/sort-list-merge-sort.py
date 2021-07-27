# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Summary:-
    Basic Merge Sort. Although this uses O(N) Space due to recursion. Bottom Up approach. We can change the
    the dummy variable approach to merge the list in place.
"""
class Solution:
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while(h1 and h2):
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
        
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        
        # Whichever list is remaining
        tail.next = h1 or h2
        return dummy.next
        
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev, slow, fast = None, head, head        
        while(fast and fast.next):
            prev, slow, fast = slow, slow.next, fast.next.next        
        prev.next = None
        
        return self.merge(*map(self.sortList, (head, slow)))
