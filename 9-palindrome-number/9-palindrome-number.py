class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        reverseNum = 0
        temp = x
        while(temp > 0):
            reverseNum = reverseNum*10 + temp%10
            temp //= 10
            
        if reverseNum == x:
            return True
        
        else:
            return False