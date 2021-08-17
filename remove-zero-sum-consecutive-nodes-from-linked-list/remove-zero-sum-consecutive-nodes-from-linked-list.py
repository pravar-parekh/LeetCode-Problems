# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        cur = head
        
        while(cur):
            arr.append(cur.val)
            cur = cur.next
            
        arr[:] = self.subArraySum(arr, 0)
        
        if not arr:
            return None
        
        head = ListNode(arr[0])
        cur = head
        for i in range(1,len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        
        return head
    
    def subArraySum(self, arr, k):
        l,r = 0, 0
        sum_ = 0
        i = 0
        while(l<len(arr)):
            r = l
            while(r < len(arr)):
                sum_ = sum(arr[l:r+1])
                if sum_ == k:
                    arr[:] = arr[0:l] + arr[r+1:]
                    r = l
                    sum_ = 0
                
                else: 
                    r += 1      
            l += 1
        return arr
             