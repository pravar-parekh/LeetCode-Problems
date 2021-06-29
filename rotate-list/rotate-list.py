# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    ****Find Total Nodes Solution (Can use fast-slow as well)****
    
    Params:- 
        head : ListNode
            Head of the list
        k : int
            Rotate in reverse direction by k
        
    Returns:-
        ListNode
            Head of the new list
            
    Summary:-
        If list is empty return None. First find total number of elements in the list.
        Then now since if k is a multiple of total, the list won't change take k = k%total.
        This saves us extra computation. Now connect head and tail elements so traversing
        the list becomes easy. Now since the element where we would need to break will be
        complement of k, i.e. total - k, which is k_ , move to the k_ element from the head,
        destroy the connection between the k_ element and it's next and make new head the
        next element. 
'''
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
        k_ = total - k
        
        if k_ == 0:
            return head
        
        x.next = head
        x = head
        new_total = 0

        count = 1
        while (count < k_):
            print(count)
            count += 1
            x = x.next
            
        head_new = x.next
        x.next = None
            
        return head_new
