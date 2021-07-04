# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    Params:-
        head : ListNode
            Head of the linked list
        
    Returns:-
        Bool
            True if palindrome, false if not a palindrome
        
    Summary:-
        First we find the midpoint of the linked list by using the fast and slow pointer 
        method. Then when fast pointer reaches the end and slow is at middle, we reverse
        the list from the slow element. Now since we have a reversed second half of the
        list, then the first and the second half should be the same. The first starts with
        head, and the second half starts with prev (since first is the same whereas second
        was reversed and slow is none whereas prev is the last element of the original list).
        Now we simply iterate and check if all elements equal, if unequal then we return false.
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while (fast != None and fast.next!= None):
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while (slow != None):
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_
        
        while(prev != None):
            print(prev.val)
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        
        return True