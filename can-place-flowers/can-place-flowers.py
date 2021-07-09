'''
    Summary:-
        Iterate through the list, if a 0 has 0 on both sides of it then make it one and,
        decrease the n. If n <= 0 then return true. Adding 0 at the end and beginning
        makes the if statement way better by not having to check border conditions.
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        length = len(flowerbed)
        
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, length + 1):
            if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            
            if n<=0: return True
        
        return False
                