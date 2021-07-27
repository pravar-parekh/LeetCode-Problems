# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Summary:-
    Sort of a cheat approach. Simply copy the list to an array and sort the array. This
    is apparently done faster than sorting the list itself. This is due to how array is
    cached. So its way better to do it this way. Not sure if this should be done in an
    interview.
    
    https://leetcode.com/problems/insertion-sort-list/discuss/46429/Thoughts-from-a-Google-interviewer
    
    "You could for sure talk about it in the interview and clear it out before jumping into    
    sorting a list. But in the end, you end up doing what he wants you to do(Say he doesn't 
    want you to use Extra Space).

    Also, For example, you could talk about the following comparison of copying a list to array 
    vs sorting the list : 
    http://stackoverflow.com/questions/1525117/whats-the-fastest-algorithm-for-sorting-a-linked-list.

    In my opinion, it's better to just put all the pros/cons on the table, and ask him which 
    one he actually needs."
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        array = []
        
        cur = head
        while(cur):
            array.append(cur.val)
            cur = cur.next
            
        array = sorted(array)
        
        cur = head
        i = 0
        while(cur):
            cur.val = array[i]
            cur = cur.next
            i += 1

        return head